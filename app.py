from flask import Flask, render_template, request, jsonify
from skyfield.api import load
import numpy as np
from datetime import datetime
from geopy.geocoders import Nominatim
import ssl
import json

import os
import uuid
from astro_expert import (
    get_dignity,
    build_expert_natal_dossier,
    compute_transits_report,
    compute_single_entity_transit_resonance,
    build_interaction_dossier,
    ELON_MUSK_CASE_STUDY,
)

app = Flask(__name__)

APP_VERSION = "2.5.2"

# --- FILE PATHS & DATA LOADING ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CITIES_FILE = os.path.join(BASE_DIR, 'cities.json')
SAVED_ANALYSES_FILE = os.path.join(BASE_DIR, 'saved_analyses.json')
SAVED_PEOPLE_FILE = os.path.join(BASE_DIR, 'saved_people.json')

# Load Curated World Cities
CITIES_DATA = []
if os.path.exists(CITIES_FILE):
    try:
        with open(CITIES_FILE, 'r', encoding='utf-8') as f:
            CITIES_DATA = json.load(f)
        print(f"Loaded {len(CITIES_DATA)} curated world cities.")
    except Exception as err:
        print(f"Error loading cities.json: {err}")

def find_city_in_db(city_str):
    """Find pre-verified city by exact or substring match."""
    clean = city_str.strip().lower()
    for c in CITIES_DATA:
        if c['display'].lower() == clean or c['name'].lower() == clean:
            return c
    for c in CITIES_DATA:
        if clean in c['display'].lower() or c['name'].lower() in clean:
            return c
    return None

def get_storage_path(filename):
    """
    Returns path for reading/writing JSON state.
    On Vercel (or read-only environments), copies to /tmp so writes succeed.
    """
    local_path = os.path.join(BASE_DIR, filename)
    if os.environ.get("VERCEL") or not os.access(BASE_DIR, os.W_OK):
        tmp_dir = os.environ.get("TMPDIR", "/tmp")
        tmp_path = os.path.join(tmp_dir, filename)
        if not os.path.exists(tmp_path) and os.path.exists(local_path):
            try:
                import shutil
                shutil.copyfile(local_path, tmp_path)
            except Exception:
                pass
        return tmp_path if os.path.exists(tmp_path) else local_path
    return local_path

def load_saved_analyses():
    target = get_storage_path('saved_analyses.json')
    if not os.path.exists(target):
        return []
    try:
        with open(target, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as err:
        print(f"Error reading {target}: {err}")
        return []

def save_analyses_to_file(data):
    target = get_storage_path('saved_analyses.json')
    try:
        with open(target, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as err:
        print(f"Notice: Could not write to {target} (environment may be read-only): {err}")

def load_saved_people():
    target = get_storage_path('saved_people.json')
    if not os.path.exists(target):
        return []
    try:
        with open(target, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as err:
        print(f"Error reading {target}: {err}")
        return []

def save_people_to_file(data):
    target = get_storage_path('saved_people.json')
    try:
        with open(target, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as err:
        print(f"Notice: Could not write to {target} (environment may be read-only): {err}")

def upsert_person_record(person_data):
    """Helper to save or update an individual person profile in saved_people.json."""
    if not person_data or not person_data.get("name"):
        return None
    people = load_saved_people()
    p_name = str(person_data.get("name", "")).strip()
    p_id = person_data.get("id")
    
    # Try finding existing record by id first, then by exact name
    idx = None
    if p_id:
        idx = next((i for i, x in enumerate(people) if x.get("id") == p_id), None)
    if idx is None:
        idx = next((i for i, x in enumerate(people) if x.get("name", "").strip().lower() == p_name.lower()), None)
        
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    if idx is not None:
        record = people[idx]
        record["name"] = p_name
        if "date" in person_data and person_data["date"]: record["date"] = person_data["date"]
        if "time" in person_data and person_data["time"]: record["time"] = person_data["time"]
        if "city" in person_data and person_data["city"]: record["city"] = person_data["city"]
        if "tz" in person_data and person_data["tz"]: record["tz"] = person_data["tz"]
        record["updated_at"] = now_str
        record["version"] = APP_VERSION
        people[idx] = record
    else:
        new_id = p_id or f"person-{str(uuid.uuid4())[:8]}"
        record = {
            "id": new_id,
            "name": p_name,
            "date": person_data.get("date", ""),
            "time": person_data.get("time", "12:00"),
            "city": person_data.get("city", ""),
            "tz": person_data.get("tz", "+03:00"),
            "created_at": now_str,
            "version": APP_VERSION
        }
        people.insert(0, record)
        
    save_people_to_file(people)
    return record

# --- CONFIG & EPHEMERIS LOADING ---
# Fix SSL for geopy
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

geolocator = Nominatim(user_agent="astro_match_pro_v3", ssl_context=ctx)

# Load NASA Ephemeris
DE421_PATH = os.path.join(BASE_DIR, 'de421.bsp')
print(f"Loading NASA Ephemeris data ({DE421_PATH})...")
eph = load(DE421_PATH)
earth = eph['earth']

# --- ASTROLOGICAL METADATA ---
ZODIAC_DATA = [
    {"name": "Aries", "symbol": "♈", "element": "fire", "quality": "cardinal", "color": "#ef4444", "start": 0},
    {"name": "Taurus", "symbol": "♉", "element": "earth", "quality": "fixed", "color": "#10b981", "start": 30},
    {"name": "Gemini", "symbol": "♊", "element": "air", "quality": "mutable", "color": "#38bdf8", "start": 60},
    {"name": "Cancer", "symbol": "♋", "element": "water", "quality": "cardinal", "color": "#818cf8", "start": 90},
    {"name": "Leo", "symbol": "♌", "element": "fire", "quality": "fixed", "color": "#f59e0b", "start": 120},
    {"name": "Virgo", "symbol": "♍", "element": "earth", "quality": "mutable", "color": "#059669", "start": 150},
    {"name": "Libra", "symbol": "♎", "element": "air", "quality": "cardinal", "color": "#0ea5e9", "start": 180},
    {"name": "Scorpio", "symbol": "♏", "element": "water", "quality": "fixed", "color": "#6366f1", "start": 210},
    {"name": "Sagittarius", "symbol": "♐", "element": "fire", "quality": "mutable", "color": "#d97706", "start": 240},
    {"name": "Capricorn", "symbol": "♑", "element": "earth", "quality": "cardinal", "color": "#047857", "start": 270},
    {"name": "Aquarius", "symbol": "♒", "element": "air", "quality": "fixed", "color": "#0284c7", "start": 300},
    {"name": "Pisces", "symbol": "♓", "element": "water", "quality": "mutable", "color": "#4f46e5", "start": 330},
]

PLANETS_CONFIG = {
    'Sun': {'target': 'sun', 'symbol': '☉', 'color': '#fbbf24', 'category': 'luminary', 'weight': 1.2},
    'Moon': {'target': 'moon', 'symbol': '☽', 'color': '#f1f5f9', 'category': 'luminary', 'weight': 1.2},
    'Mercury': {'target': 'mercury', 'symbol': '☿', 'color': '#38bdf8', 'category': 'personal', 'weight': 0.9},
    'Venus': {'target': 'venus', 'symbol': '♀', 'color': '#f472b6', 'category': 'personal', 'weight': 1.3},
    'Mars': {'target': 'mars', 'symbol': '♂', 'color': '#ef4444', 'category': 'personal', 'weight': 1.1},
    'Jupiter': {'target': 'jupiter barycenter', 'symbol': '♃', 'color': '#fb923c', 'category': 'social', 'weight': 1.0},
    'Saturn': {'target': 'saturn barycenter', 'symbol': '♄', 'color': '#eab308', 'category': 'social', 'weight': 1.0},
    'Uranus': {'target': 'uranus barycenter', 'symbol': '♅', 'color': '#06b6d4', 'category': 'outer', 'weight': 0.7},
    'Neptune': {'target': 'neptune barycenter', 'symbol': '♆', 'color': '#818cf8', 'category': 'outer', 'weight': 0.7},
    'Pluto': {'target': 'pluto barycenter', 'symbol': '♇', 'color': '#a855f7', 'category': 'outer', 'weight': 0.8},
}

ASPECT_CONFIGS = {
    'Conjunction': {'angle': 0, 'max_orb': 7.5, 'nature': 'harmonious', 'color': '#fbbf24', 'base_points': 10},
    'Opposition': {'angle': 180, 'max_orb': 7.0, 'nature': 'challenging', 'color': '#f43f5e', 'base_points': -3},
    'Trine': {'angle': 120, 'max_orb': 7.0, 'nature': 'harmonious', 'color': '#10b981', 'base_points': 9},
    'Square': {'angle': 90, 'max_orb': 6.5, 'nature': 'challenging', 'color': '#ef4444', 'base_points': -6},
    'Sextile': {'angle': 60, 'max_orb': 4.5, 'nature': 'harmonious', 'color': '#06b6d4', 'base_points': 6},
}

# Detailed Synastry Archetype Interpretations
CUSTOM_INTERPRETATIONS = {
    "Sun-Moon-Conjunction": "The celestial marriage aspect. Effortless soul-level mutual understanding, deep emotional harmony, and instinctive alignment.",
    "Sun-Moon-Trine": "Natural, fluid resonance between ego and emotions. You instinctively validate and comfort each other's inner worlds.",
    "Sun-Moon-Sextile": "Friendly, cooperative affinity. You communicate intentions cleanly and support one another's life growth.",
    "Sun-Moon-Opposition": "Intense magnetic polarity. Profound attraction mixed with distinct worldviews; creates growth through complementary differences.",
    "Sun-Moon-Square": "Creative tension between will and vulnerability. Requires conscious empathy to bridge differing emotional temperaments.",
    
    "Venus-Mars-Conjunction": "Electric physical attraction and raw romantic magnetism. Immediate spark with powerful sensual chemistry.",
    "Venus-Mars-Trine": "Golden romantic flow. Seduction, desire, and affection align effortlessly, creating sustained passion without hostility.",
    "Venus-Mars-Sextile": "Playful, spirited chemistry. Flirtatious ease with natural appreciation for each other's romantic style.",
    "Venus-Mars-Square": "High-octane sexual friction. Hot, fiery, and intoxicating passion that demands constructive channels to prevent petty clashes.",
    "Venus-Mars-Opposition": "Irresistible magnetic pull across polar opposites. The chase is exhilarating, though balancing affection and ego takes patience.",

    "Venus-Venus-Conjunction": "Shared aesthetic tastes, love languages, and social rhythms. You experience joy and luxury through the same lens.",
    "Venus-Venus-Trine": "Effortless tenderness and reciprocal affection. A deeply soothing bond that softens daily stress.",
    "Venus-Venus-Square": "Contrasting affection styles or differing spending/social habits. Fun and stimulating once you embrace varied tastes.",
    
    "Moon-Moon-Conjunction": "Telepathic emotional kinship. You feel like 'home' to one another and mirror each other's vulnerabilities.",
    "Moon-Moon-Trine": "Profound emotional safety, tenderness, and intuitive trust. You naturally nurture each other.",
    "Moon-Moon-Square": "Differing domestic habits and emotional processing speeds. Demands gentle listening and spacious boundaries.",
    "Moon-Moon-Opposition": "Emotional seesaw that builds deep awareness. One acts as the anchor while the other expresses, swapping instinctively.",

    "Sun-Sun-Trine": "Harmonious core values, mutual admiration, and shared vision of purposeful living.",
    "Sun-Sun-Conjunction": "Powerful vitality and shared spotlight. You energize one another, though space for individual sovereignty is essential.",
    "Sun-Sun-Square": "Dynamic challenge of wills. Strong personalities push each other toward peak ambition, provided competition is kept healthy.",
    "Sun-Sun-Opposition": "Fascinating mirror dynamic. Each partner sees unexpressed parts of themselves reflected in the other.",

    "Mercury-Mercury-Conjunction": "Rapid mental wavelength synchronization. Hours vanish in conversation as your thought patterns finish each other's sentences.",
    "Mercury-Mercury-Trine": "Stimulating intellectual rapport. Collaboration on creative, analytical, or practical projects flows with ease.",
    "Mercury-Mercury-Square": "Spirited debates and differing communication cadences. Highly stimulating, though active listening is key to avoid misunderstandings.",

    "Jupiter-Sun-Trine": "Abundant good fortune, optimism, and generous mutual encouragement. You expand each other's horizons and luck.",
    "Jupiter-Moon-Trine": "Heartwarming warmth, humor, and psychological comfort. A relationship imbued with good cheer and forgiveness.",
    "Saturn-Sun-Trine": "Bedrock of enduring commitment, loyalty, and mutual respect. Built to withstand time and real-world trials.",
    "Saturn-Venus-Trine": "Unshakable fidelity and grounded love. Affection deepens into lasting mutual loyalty and shared responsibility.",
    "Saturn-Venus-Square": "Heavy karmic lessons regarding trust and timing. Affection may feel cautious, but matures with dedication.",
    "Pluto-Venus-Conjunction": "Profound, transformative passion with obsessive or hypnotic intensity. Love that leaves neither partner unchanged.",
    "Pluto-Venus-Trine": "Deep emotional and physical depth. Passion that renews and heals past heartaches through total trust.",
    "Neptune-Venus-Trine": "Poetic, fairytale romance and unconditional artistic or spiritual devotion.",
    "Uranus-Venus-Trine": "Exciting, unconventional romantic electricity. Zero boredom, high personal freedom, and electric chemistry.",
}

def format_zodiac(lon_deg):
    """Convert ecliptic longitude (0-360) into sign, deg, min, symbol."""
    norm_deg = lon_deg % 360
    sign_idx = int(norm_deg // 30) % 12
    sign_info = ZODIAC_DATA[sign_idx]
    deg_in_sign = int(norm_deg % 30)
    min_in_sign = int(round((norm_deg % 1) * 60))
    if min_in_sign == 60:
        deg_in_sign += 1
        min_in_sign = 0
    return {
        "sign": sign_info["name"],
        "symbol": sign_info["symbol"],
        "element": sign_info["element"],
        "color": sign_info["color"],
        "deg": deg_in_sign,
        "min": min_in_sign,
        "formatted": f"{deg_in_sign}° {min_in_sign:02d}' {sign_info['symbol']} {sign_info['name']}",
        "raw": float(norm_deg)
    }

def calculate_angles_and_houses(t, lat, lon, coord_system='tropical'):
    """
    Calculate Ascendant, Midheaven (MC), Descendant, Imum Coeli (IC),
    and 12 Equal House Cusps. Supports 'tropical' (GAST) and 'j2000' (GMST).
    """
    gast_hours = t.gast if coord_system == 'tropical' else t.gmst
    lst_hours = (gast_hours + lon / 15.0) % 24
    ramc_deg = (lst_hours * 15.0) % 360
    eps_rad = np.radians(23.4392911) # Obliquity of Ecliptic
    
    ramc_rad = np.radians(ramc_deg)
    lat_rad = np.radians(lat)
    
    # Ascendant
    num = np.cos(ramc_rad)
    den = -((np.sin(ramc_rad) * np.cos(eps_rad)) + (np.tan(lat_rad) * np.sin(eps_rad)))
    asc_deg = float(np.degrees(np.arctan2(num, den)) % 360)
    
    # Midheaven (MC)
    mc_deg = float(np.degrees(np.arctan2(np.sin(ramc_rad), np.cos(ramc_rad) * np.cos(eps_rad))) % 360)
    
    # Descendant and IC
    dsc_deg = float((asc_deg + 180) % 360)
    ic_deg = float((mc_deg + 180) % 360)
    
    # Porphyry Houses Calculation
    def normalize_angle(deg):
        return deg % 360
        
    arc_asc_ic = normalize_angle(ic_deg - asc_deg)
    arc_ic_dsc = normalize_angle(dsc_deg - ic_deg)
    arc_dsc_mc = normalize_angle(mc_deg - dsc_deg)
    arc_mc_asc = normalize_angle(asc_deg - mc_deg)
    
    cusps = []
    
    # Q1: ASC to IC
    cusps.append(asc_deg)
    cusps.append(normalize_angle(asc_deg + arc_asc_ic / 3.0))
    cusps.append(normalize_angle(asc_deg + 2.0 * arc_asc_ic / 3.0))
    
    # Q2: IC to DSC
    cusps.append(ic_deg)
    cusps.append(normalize_angle(ic_deg + arc_ic_dsc / 3.0))
    cusps.append(normalize_angle(ic_deg + 2.0 * arc_ic_dsc / 3.0))
    
    # Q3: DSC to MC
    cusps.append(dsc_deg)
    cusps.append(normalize_angle(dsc_deg + arc_dsc_mc / 3.0))
    cusps.append(normalize_angle(dsc_deg + 2.0 * arc_dsc_mc / 3.0))
    
    # Q4: MC to ASC
    cusps.append(mc_deg)
    cusps.append(normalize_angle(mc_deg + arc_mc_asc / 3.0))
    cusps.append(normalize_angle(mc_deg + 2.0 * arc_mc_asc / 3.0))
    
    houses = []
    for i in range(12):
        cusp_deg = cusps[i]
        houses.append({
            "house": i + 1,
            "cusp": round(float(cusp_deg), 2),
            "zodiac": format_zodiac(cusp_deg)
        })
        
    return {
        "asc": asc_deg,
        "mc": mc_deg,
        "dsc": dsc_deg,
        "ic": ic_deg,
        "houses": houses
    }

def get_house_for_lon(lon_deg, cusps_list):
    """Determine which unequal house (1-12) an ecliptic longitude falls into."""
    lon_deg = lon_deg % 360
    for i in range(12):
        cusp_current = cusps_list[i]
        cusp_next = cusps_list[(i + 1) % 12]
        if cusp_current < cusp_next:
            if cusp_current <= lon_deg < cusp_next:
                return i + 1
        else:
            if lon_deg >= cusp_current or lon_deg < cusp_next:
                return i + 1
    return 1

def _calculate_chart_system(t, lat, lon, coord_system='tropical', t_next=None):
    """Compute angles, houses, planets, lunar nodes, dignities, retrogrades, and expert dossier."""
    angles = calculate_angles_and_houses(t, lat, lon, coord_system=coord_system)
    asc_deg = angles["asc"]
    cusps_deg_list = [h["cusp"] for h in angles["houses"]]
    
    planets_list = []
    planets_dict = {}
    
    for p_name, p_info in PLANETS_CONFIG.items():
        p_obj = eph[p_info['target']]
        if coord_system == 'tropical':
            apparent = earth.at(t).observe(p_obj).apparent()
            _, lon_ecl, _ = apparent.ecliptic_latlon('date')
            if t_next is not None:
                _, lon_ecl_next, _ = earth.at(t_next).observe(p_obj).apparent().ecliptic_latlon('date')
            else:
                lon_ecl_next = lon_ecl
        else: # 'j2000'
            astrometric = earth.at(t).observe(p_obj)
            _, lon_ecl, _ = astrometric.ecliptic_latlon()
            if t_next is not None:
                _, lon_ecl_next, _ = earth.at(t_next).observe(p_obj).ecliptic_latlon()
            else:
                lon_ecl_next = lon_ecl
            
        deg = float(lon_ecl.degrees % 360)
        deg_next = float(lon_ecl_next.degrees % 360)
        daily_speed = ((deg_next - deg + 180.0) % 360.0 - 180.0) / 0.1 if t_next is not None else 1.0
        is_retrograde = bool(daily_speed < 0 and p_name not in ('Sun', 'Moon'))

        zodiac = format_zodiac(deg)
        house_num = get_house_for_lon(deg, cusps_deg_list)
        dignity = get_dignity(p_name, zodiac["sign"])
        
        planet_entry = {
            "name": p_name,
            "symbol": p_info["symbol"],
            "color": p_info["color"],
            "category": p_info["category"],
            "lon": round(deg, 2),
            "sign": zodiac["sign"],
            "sign_symbol": zodiac["symbol"],
            "sign_element": zodiac["element"],
            "sign_deg": zodiac["deg"],
            "sign_min": zodiac["min"],
            "deg": zodiac["deg"],
            "min": zodiac["min"],
            "sign_color": zodiac["color"],
            "formatted": zodiac["formatted"],
            "house": house_num,
            "retrograde": is_retrograde,
            "speed": round(float(daily_speed), 3),
            "dignity": dignity
        }
        planets_list.append(planet_entry)
        planets_dict[p_name] = planet_entry

    # Compute Lunar North Node (Mean Ascending Node)
    T_cent = (t.tt - 2451545.0) / 36525.0
    nn_trop = (125.04452 - 1934.136261 * T_cent + 0.0020708 * (T_cent ** 2) + (T_cent ** 3) / 450000.0) % 360.0
    if coord_system == 'j2000':
        prec_deg = (1.396971 * T_cent) % 360.0
        nn_deg = (nn_trop - prec_deg) % 360.0
    else:
        nn_deg = float(nn_trop)
    nn_zodiac = format_zodiac(nn_deg)
    north_node_entry = {
        "name": "North Node",
        "symbol": "☊",
        "color": "#c084fc",
        "category": "node",
        "lon": round(nn_deg, 2),
        "sign": nn_zodiac["sign"],
        "sign_symbol": nn_zodiac["symbol"],
        "sign_element": nn_zodiac["element"],
        "sign_deg": nn_zodiac["deg"],
        "sign_min": nn_zodiac["min"],
        "deg": nn_zodiac["deg"],
        "min": nn_zodiac["min"],
        "sign_color": nn_zodiac["color"],
        "formatted": nn_zodiac["formatted"],
        "house": get_house_for_lon(nn_deg, cusps_deg_list),
        "retrograde": True,
        "speed": -0.053,
        "dignity": {"status": "peregrine", "label_en": "Karmic Node", "label_he": "ראש הדרקון", "color": "#c084fc"}
    }

    # Add Ascendant and MC as special points
    asc_zodiac = format_zodiac(asc_deg)
    asc_entry = {
        "name": "Ascendant",
        "symbol": "ASC",
        "color": "#ec4899",
        "category": "angle",
        "lon": round(asc_deg, 2),
        "sign": asc_zodiac["sign"],
        "sign_symbol": asc_zodiac["symbol"],
        "sign_element": asc_zodiac["element"],
        "sign_deg": asc_zodiac["deg"],
        "sign_min": asc_zodiac["min"],
        "deg": asc_zodiac["deg"],
        "min": asc_zodiac["min"],
        "sign_color": asc_zodiac["color"],
        "formatted": asc_zodiac["formatted"],
        "house": 1
    }
    
    mc_zodiac = format_zodiac(angles["mc"])
    mc_entry = {
        "name": "Midheaven",
        "symbol": "MC",
        "color": "#8b5cf6",
        "category": "angle",
        "lon": round(angles["mc"], 2),
        "sign": mc_zodiac["sign"],
        "sign_symbol": mc_zodiac["symbol"],
        "sign_element": mc_zodiac["element"],
        "sign_deg": mc_zodiac["deg"],
        "sign_min": mc_zodiac["min"],
        "deg": mc_zodiac["deg"],
        "min": mc_zodiac["min"],
        "sign_color": mc_zodiac["color"],
        "formatted": mc_zodiac["formatted"],
        "house": 10
    }

    # Natal aspects for this individual (including ASC, MC, and North Node)
    all_points = planets_list + [asc_entry, mc_entry, north_node_entry]
    natal_aspects = []
    for i in range(len(all_points)):
        for j in range(i + 1, len(all_points)):
            pt1 = all_points[i]
            pt2 = all_points[j]
            # Skip ASC-MC aspect since they are structural axes
            if {pt1["name"], pt2["name"]} == {"Ascendant", "Midheaven"}:
                continue
            diff = abs(pt1["lon"] - pt2["lon"])
            diff = min(diff, 360.0 - diff)
            
            for asp_name, asp_cfg in ASPECT_CONFIGS.items():
                orb = abs(diff - asp_cfg["angle"])
                if orb <= asp_cfg["max_orb"]:
                    natal_aspects.append({
                        "p1": pt1["name"],
                        "p1_symbol": pt1["symbol"],
                        "p1_lon": pt1["lon"],
                        "p2": pt2["name"],
                        "p2_symbol": pt2["symbol"],
                        "p2_lon": pt2["lon"],
                        "aspect": asp_name,
                        "angle": asp_cfg["angle"],
                        "orb": round(orb, 1),
                        "color": asp_cfg["color"],
                        "nature": asp_cfg["nature"]
                    })
                    break

    sys_result = {
        "system": coord_system,
        "asc": round(asc_deg, 2),
        "mc": round(angles["mc"], 2),
        "dsc": round(angles["dsc"], 2),
        "ic": round(angles["ic"], 2),
        "houses": angles["houses"],
        "planets": planets_list,
        "planets_dict": planets_dict,
        "asc_point": asc_entry,
        "mc_point": mc_entry,
        "north_node": north_node_entry,
        "natal_aspects": natal_aspects,
        # Big Three shorthand
        "sun_sign": planets_dict["Sun"]["sign"],
        "moon_sign": planets_dict["Moon"]["sign"],
        "asc_sign": asc_zodiac["sign"],
        "mc_sign": mc_zodiac["sign"],
    }
    sys_result["expert_dossier"] = build_expert_natal_dossier(sys_result)
    return sys_result

def compute_chart(name, date_str, time_str, tz_str, city_str):
    """Calculates all planetary coordinates, angles, houses, natal aspects, and expert synthesis."""
    # Resolve City Coordinates (Curated DB first, then live OpenStreetMap/Nominatim fallback)
    matched_city = find_city_in_db(city_str)
    if matched_city:
        lat, lon = matched_city['lat'], matched_city['lon']
        address = matched_city['display']
        source = "Curated Database"
    else:
        location = geolocator.geocode(city_str)
        if not location:
            raise ValueError(f"Could not locate '{city_str}' on OpenStreetMap or local database. Please check spelling or specify country (e.g., 'Kiryat Gat, Israel').")
        lat, lon = location.latitude, location.longitude
        address = location.address
        source = "OpenStreetMap"
    
    # Parse date and time
    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    
    # Parse timezone offset e.g. +02:00, -05:00, +2, -5
    try:
        tz_clean = tz_str.strip()
        sign = 1 if tz_clean[0] != '-' else -1
        core = tz_clean.lstrip('+-')
        if ':' in core:
            parts = core.split(':')
            h = int(parts[0])
            m = int(parts[1])
        else:
            h = int(core)
            m = 0
        total_offset = sign * (h + m / 60.0)
    except Exception:
        total_offset = 0.0
        
    ts = load.timescale()
    t = ts.utc(dt.year, dt.month, dt.day, dt.hour - total_offset, dt.minute)
    t_next = ts.tt_jd(t.tt + 0.1)
    
    # Compute both Tropical (Date / Astro.com) and J2000 (Astrometric) systems
    trop_data = _calculate_chart_system(t, lat, lon, coord_system='tropical', t_next=t_next)
    j2000_data = _calculate_chart_system(t, lat, lon, coord_system='j2000', t_next=t_next)

    return {
        "name": name,
        "date": date_str,
        "time": time_str,
        "tz": tz_str,
        "city": city_str,
        "location_address": address,
        "location_source": source,
        "lat": round(lat, 4),
        "lon": round(lon, 4),
        "systems": {
            "tropical": trop_data,
            "j2000": j2000_data
        },
        # Default top-level properties to tropical for backwards compatibility
        **trop_data
    }

def _calculate_synastry_single(c1_sys, c2_sys, name1="Entity A", name2="Entity B"):
    """Calculates inter-chart aspects, compatibility score breakdown, house overlays, and interpretations."""
    aspects = []
    
    # Points to compare (including ASC, MC, and North Node)
    pts1 = c1_sys["planets"] + [c1_sys["asc_point"], c1_sys["mc_point"]]
    if c1_sys.get("north_node"):
        pts1.append(c1_sys["north_node"])
    pts2 = c2_sys["planets"] + [c2_sys["asc_point"], c2_sys["mc_point"]]
    if c2_sys.get("north_node"):
        pts2.append(c2_sys["north_node"])
    
    raw_score = 0.0
    pos_weighted_score = 0.0
    neg_weighted_score = 0.0
    cat_tracker = {
        "chemistry": {"pos": 6.0, "neg": 6.0},
        "emotional": {"pos": 6.0, "neg": 6.0},
        "intellectual": {"pos": 6.0, "neg": 6.0},
        "stability": {"pos": 6.0, "neg": 6.0}
    }
    
    for p1 in pts1:
        for p2 in pts2:
            diff = abs(p1["lon"] - p2["lon"])
            diff = min(diff, 360.0 - diff)
            
            for asp_name, asp_cfg in ASPECT_CONFIGS.items():
                orb = abs(diff - asp_cfg["angle"])
                if orb <= asp_cfg["max_orb"]:
                    # Compute tightness factor (1.0 = exact, 0.0 = at orb boundary)
                    tightness = max(0.0, 1.0 - (orb / asp_cfg["max_orb"]))
                    
                    # Look up custom interpretation and key
                    pair_key1 = f"{p1['name']}-{p2['name']}-{asp_name}"
                    pair_key2 = f"{p2['name']}-{p1['name']}-{asp_name}"
                    if pair_key1 in CUSTOM_INTERPRETATIONS:
                        aspect_key = pair_key1
                        meaning = CUSTOM_INTERPRETATIONS[pair_key1]
                    elif pair_key2 in CUSTOM_INTERPRETATIONS:
                        aspect_key = pair_key2
                        meaning = CUSTOM_INTERPRETATIONS[pair_key2]
                    else:
                        aspect_key = f"generic-{asp_name}"
                        meaning = f"Dynamic planetary link: {p1['name']} {asp_name} {p2['name']} creates active energy exchange between {p1['name']}'s drive and {p2['name']}'s essence."
                    
                    # Point calculation with personal planet weighting
                    w1 = 1.4 if p1['name'] in ['Sun', 'Moon', 'Venus', 'Mars', 'Ascendant'] else (1.0 if p1['name'] in ['Mercury', 'Jupiter', 'Saturn', 'Midheaven'] else 0.5)
                    w2 = 1.4 if p2['name'] in ['Sun', 'Moon', 'Venus', 'Mars', 'Ascendant'] else (1.0 if p2['name'] in ['Mercury', 'Jupiter', 'Saturn', 'Midheaven'] else 0.5)
                    weight = w1 * w2
                    pt = asp_cfg["base_points"] * tightness * weight
                    abs_pt = abs(asp_cfg["base_points"]) * tightness * weight
                    raw_score += pt

                    pair_names = {p1['name'], p2['name']}
                    if asp_cfg["nature"] == "harmonious":
                        pos_weighted_score += abs_pt
                        if pair_names & {'Venus', 'Mars'}:
                            cat_tracker["chemistry"]["pos"] += abs_pt * 1.5
                        if pair_names & {'Moon', 'Neptune', 'Sun'}:
                            cat_tracker["emotional"]["pos"] += abs_pt * 1.3
                        if pair_names & {'Mercury', 'Uranus'}:
                            cat_tracker["intellectual"]["pos"] += abs_pt * 1.4
                        if pair_names & {'Saturn', 'Jupiter', 'Ascendant', 'Midheaven', 'North Node'}:
                            cat_tracker["stability"]["pos"] += abs_pt * 1.3
                    else:
                        neg_weighted_score += abs_pt * 1.15
                        if pair_names & {'Venus', 'Mars'}:
                            cat_tracker["chemistry"]["neg"] += abs_pt * 1.5
                        if pair_names & {'Moon', 'Neptune', 'Sun'}:
                            cat_tracker["emotional"]["neg"] += abs_pt * 1.3
                        if pair_names & {'Mercury', 'Uranus'}:
                            cat_tracker["intellectual"]["neg"] += abs_pt * 1.4
                        if pair_names & {'Saturn', 'Jupiter', 'Ascendant', 'Midheaven', 'North Node'}:
                            cat_tracker["stability"]["neg"] += abs_pt * 1.3
                    
                    aspects.append({
                        "p1_planet": p1["name"],
                        "p1_symbol": p1["symbol"],
                        "p1_lon": p1["lon"],
                        "p1_sign": p1["sign"],
                        "p2_planet": p2["name"],
                        "p2_symbol": p2["symbol"],
                        "p2_lon": p2["lon"],
                        "p2_sign": p2["sign"],
                        "aspect": asp_name,
                        "angle": asp_cfg["angle"],
                        "orb": round(orb, 1),
                        "tightness": round(tightness, 2),
                        "nature": asp_cfg["nature"],
                        "color": asp_cfg["color"],
                        "meaning": meaning,
                        "aspect_key": aspect_key,
                        "points": round(pt, 1)
                    })
                    break

    # Sort aspects by tightness
    aspects.sort(key=lambda x: x["orb"])
    
    # Normalize scores between 25 and 98% based on true harmonic-to-tension ratio
    def clamp_score(val):
        return int(max(25, min(98, round(val))))
        
    tot_weight = pos_weighted_score + neg_weighted_score
    harmony_ratio = (pos_weighted_score / tot_weight) if tot_weight > 0 else 0.5
    overall_pct = clamp_score(25 + (harmony_ratio * 72))

    chemistry_pct = clamp_score(25 + ((cat_tracker["chemistry"]["pos"] / (cat_tracker["chemistry"]["pos"] + cat_tracker["chemistry"]["neg"])) * 72))
    emotional_pct = clamp_score(25 + ((cat_tracker["emotional"]["pos"] / (cat_tracker["emotional"]["pos"] + cat_tracker["emotional"]["neg"])) * 72))
    intellectual_pct = clamp_score(25 + ((cat_tracker["intellectual"]["pos"] / (cat_tracker["intellectual"]["pos"] + cat_tracker["intellectual"]["neg"])) * 72))
    stability_pct = clamp_score(25 + ((cat_tracker["stability"]["pos"] / (cat_tracker["stability"]["pos"] + cat_tracker["stability"]["neg"])) * 72))
    
    # Overall summary verdict
    if overall_pct >= 85:
        verdict_key = "verdict_85"
        verdict = "Exceptional Cosmic Affinity: Rare magnetic harmony with deep mutual understanding and lasting soul connection."
    elif overall_pct >= 70:
        verdict_key = "verdict_70"
        verdict = "High Astrological Resonance: Natural chemistry and supportive aspects outshine minor differences."
    elif overall_pct >= 55:
        verdict_key = "verdict_55"
        verdict = "Dynamic & Complementary Bond: Meaningful passion paired with growth opportunities that require conscious empathy."
    else:
        verdict_key = "verdict_0"
        verdict = "Karmic Growth Catalyst: Intense friction and distinct temperaments; great personal transformation if communication is nurtured."

    syn_dict = {
        "aspects": aspects,
        "overall_score": overall_pct,
        "chemistry_score": chemistry_pct,
        "emotional_score": emotional_pct,
        "intellectual_score": intellectual_pct,
        "stability_score": stability_pct,
        "verdict": verdict,
        "verdict_key": verdict_key,
        "raw_points": round(raw_score, 1)
    }
    interaction = build_interaction_dossier(c1_sys, c2_sys, syn_dict, name1, name2, get_house_for_lon)
    syn_dict["interaction"] = interaction
    syn_dict["power_score"] = interaction["power_score"]
    syn_dict["wealth_score"] = interaction["wealth_score"]
    return syn_dict

def calculate_synastry(c1, c2):
    """Calculates all inter-chart aspects, house overlays, and scores for both Tropical and J2000 systems."""
    name1 = c1.get("name", "Entity A")
    name2 = c2.get("name", "Entity B")
    c1_trop = c1.get("systems", {}).get("tropical", c1)
    c2_trop = c2.get("systems", {}).get("tropical", c2)
    c1_j2000 = c1.get("systems", {}).get("j2000", c1)
    c2_j2000 = c2.get("systems", {}).get("j2000", c2)

    syn_tropical = _calculate_synastry_single(c1_trop, c2_trop, name1=name1, name2=name2)
    syn_j2000 = _calculate_synastry_single(c1_j2000, c2_j2000, name1=name1, name2=name2)

    return {
        "systems": {
            "tropical": syn_tropical,
            "j2000": syn_j2000
        },
        # Default top-level fields to tropical for backwards compatibility
        **syn_tropical
    }

def calculate_transits(chart1, chart2, transit_date_str=None, transit_time_str=None):
    """Calculate Current Sky / Transit positions and Transit-to-Natal reports for both entities."""
    now = datetime.now()
    t_date = (transit_date_str or "").strip() or now.strftime("%Y-%m-%d")
    t_time = (transit_time_str or "").strip() or now.strftime("%H:%M")
    t_city = chart1.get("city", "Tel Aviv, Israel")
    t_tz = chart1.get("tz", "+02:00")

    transit_chart = compute_chart(f"Current Sky ({t_date})", t_date, t_time, t_tz, t_city)

    trop_t = transit_chart["systems"]["tropical"]
    j2000_t = transit_chart["systems"]["j2000"]

    rep_p1_trop = compute_transits_report(chart1["systems"]["tropical"], trop_t, f"{t_date} {t_time}", get_house_for_lon)
    rep_p2_trop = compute_transits_report(chart2["systems"]["tropical"], trop_t, f"{t_date} {t_time}", get_house_for_lon)

    rep_p1_j2000 = compute_transits_report(chart1["systems"]["j2000"], j2000_t, f"{t_date} {t_time}", get_house_for_lon)
    rep_p2_j2000 = compute_transits_report(chart2["systems"]["j2000"], j2000_t, f"{t_date} {t_time}", get_house_for_lon)

    return {
        "date": t_date,
        "time": t_time,
        "transit_chart": transit_chart,
        "systems": {
            "tropical": {"p1": rep_p1_trop, "p2": rep_p2_trop},
            "j2000": {"p1": rep_p1_j2000, "p2": rep_p2_j2000},
        },
        "p1": rep_p1_trop,
        "p2": rep_p2_trop,
    }

# --- ROUTES ---
@app.route('/', methods=['GET'])
@app.route('/api/index', methods=['GET'])
def index():
    now_date = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M")
    return render_template('index.html', app_version=APP_VERSION, now_date=now_date, now_time=now_time)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        now_date = datetime.now().strftime("%Y-%m-%d")
        now_time = datetime.now().strftime("%H:%M")

        transit_date = request.form.get('transit_date', now_date).strip() or now_date
        transit_time = request.form.get('transit_time', now_time).strip() or now_time

        p1_inputs = {
            'name': request.form['p1_name'].strip(),
            'date_str': request.form['p1_date'],
            'time_str': request.form['p1_time'],
            'city_str': request.form['p1_city'].strip(),
            'tz_str': request.form['p1_tz'].strip()
        }

        # Allow single-entity analysis by falling back to Current Sky if Partner B is left blank
        p2_name_raw = request.form.get('p2_name', '').strip()
        p2_date_raw = request.form.get('p2_date', '').strip()
        is_single_entity = not (p2_name_raw and p2_date_raw)
        if not is_single_entity:
            p2_inputs = {
                'name': p2_name_raw,
                'date_str': p2_date_raw,
                'time_str': request.form.get('p2_time', '12:00').strip() or '12:00',
                'city_str': request.form.get('p2_city', p1_inputs['city_str']).strip() or p1_inputs['city_str'],
                'tz_str': request.form.get('p2_tz', p1_inputs['tz_str']).strip() or p1_inputs['tz_str']
            }
        else:
            p2_inputs = {
                'name': f"Current Sky ({transit_date})",
                'date_str': transit_date,
                'time_str': transit_time,
                'city_str': p1_inputs['city_str'],
                'tz_str': p1_inputs['tz_str']
            }
        
        # Calculate individual charts
        chart1 = compute_chart(**p1_inputs)
        chart2 = compute_chart(**p2_inputs)
        chart2["is_current_sky"] = is_single_entity
        
        # Calculate Synastry / Entity Interaction
        synastry = calculate_synastry(chart1, chart2)

        # Calculate Current Date Transits
        transits = calculate_transits(chart1, chart2, transit_date, transit_time)
        
        # Calculate Single Entity Transit Resonance & Forecast if in single-entity mode
        single_resonance = None
        if is_single_entity:
            single_resonance = compute_single_entity_transit_resonance(
                chart1["systems"]["tropical"],
                transits["systems"]["tropical"]["p1"]
            )
        
        # Bundle everything for frontend visualization
        payload = {
            "chart1": chart1,
            "chart2": chart2,
            "synastry": synastry,
            "transits": transits,
            "is_single_entity": is_single_entity,
            "single_resonance": single_resonance,
            "elon_case_study": ELON_MUSK_CASE_STUDY,
            "zodiac_data": ZODIAC_DATA
        }
        
        return render_template(
            'result.html',
            p1=chart1,
            p2=chart2,
            synastry=synastry,
            transits=transits,
            is_single_entity=is_single_entity,
            single_resonance=single_resonance,
            elon_case_study=ELON_MUSK_CASE_STUDY,
            payload_json=json.dumps(payload),
            app_version=APP_VERSION
        )
        
    except Exception as e:
        import traceback
        return render_template(
            'index.html',
            error=f"Error calculating charts: {str(e)}",
            app_version=APP_VERSION,
            now_date=datetime.now().strftime("%Y-%m-%d"),
            now_time=datetime.now().strftime("%H:%M")
        )

# --- API ROUTES ---
@app.route('/api/geocode', methods=['GET'])
def api_geocode():
    """
    Verify city live across curated DB and OpenStreetMap (Nominatim).
    Tells the client exactly where it looked, if it found it, coordinates, and timezone.
    """
    q = request.args.get('q', '').strip()
    if not q or len(q) < 2:
        return jsonify({"found": False, "message": "City query is empty or too short."})
    
    # 1. Curated database check (Fastest, pre-verified)
    matched = find_city_in_db(q)
    if matched:
        return jsonify({
            "found": True,
            "source": "Curated Database",
            "name": matched["name"],
            "display": matched["display"],
            "lat": matched["lat"],
            "lon": matched["lon"],
            "tz": matched["tz"],
            "message": f"Verified in local database: {matched['display']}"
        })
        
    # 2. OpenStreetMap / Nominatim check (Worldwide coverage: towns, suburbs, villages)
    try:
        loc = geolocator.geocode(q)
        if loc:
            addr = loc.address
            lat = round(loc.latitude, 4)
            lon = round(loc.longitude, 4)
            
            # Geographic standard GMT offset without daylight saving (15 degrees per timezone hour)
            raw_offset = round(lon / 15.0)
            sign = "+" if raw_offset >= 0 else "-"
            tz_est = f"{sign}{abs(int(raw_offset)):02d}:00"
                
            return jsonify({
                "found": True,
                "source": "OpenStreetMap",
                "name": q,
                "display": loc.address,
                "lat": lat,
                "lon": lon,
                "tz": tz_est,
                "message": f"Found on OpenStreetMap: {loc.address}"
            })
        else:
            return jsonify({
                "found": False,
                "source": "OpenStreetMap & Local Database",
                "query": q,
                "message": f"Could not find '{q}' on OpenStreetMap or local list. Please check spelling or specify country (e.g. '{q}, Israel')."
            })
    except Exception as e:
        return jsonify({
            "found": False,
            "source": "OpenStreetMap Lookup",
            "query": q,
            "message": f"Geocoding service error: {str(e)}"
        })

@app.route('/api/cities', methods=['GET'])
def api_cities():
    """Return filtered cities from curated database."""
    q = request.args.get('q', '').strip().lower()
    if not q:
        return jsonify(CITIES_DATA[:80])
    matches = [
        c for c in CITIES_DATA
        if q in c['display'].lower() or q in c['name'].lower() or q in c['country'].lower()
    ]
    return jsonify(matches[:40])

@app.route('/api/analyses', methods=['GET'])
def api_get_analyses():
    """List all saved analyses."""
    return jsonify(load_saved_analyses())

@app.route('/api/analyses', methods=['POST'])
def api_save_analysis():
    """Save a new couple analysis profile."""
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "No JSON payload provided"}), 400
        
        saved = load_saved_analyses()
        analysis_id = str(uuid.uuid4())[:8]
        p2_data = data.get("p2", {})
        p2_name = str(p2_data.get("name", "")).strip()

        # Deduce analysis type: 'single_transit' vs 'synastry'
        if data.get("type"):
            analysis_type = data.get("type")
        elif not p2_name or "Current Sky" in p2_name:
            analysis_type = "single_transit"
        else:
            analysis_type = "synastry"

        now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        transit_date = data.get("transit_date") or datetime.now().strftime("%Y-%m-%d")
        transit_time = data.get("transit_time") or datetime.now().strftime("%H:%M")

        p1_name = str(data.get("p1", {}).get("name", "Individual")).strip()
        if analysis_type == "single_transit":
            default_title = f"{p1_name} — Transit Snapshot ({transit_date})"
        else:
            default_title = f"{p1_name} & {p2_name or 'Partner B'}"

        new_item = {
            "id": f"match-{analysis_id}",
            "type": analysis_type,
            "title": data.get("title") or default_title,
            "created_at": now_str,
            "transit_date": transit_date,
            "transit_time": transit_time,
            "version": data.get("version") or APP_VERSION,
            "p1": data.get("p1", {}),
            "p2": p2_data if analysis_type != "single_transit" else {},
            "notes": data.get("notes", "")
        }
        saved.insert(0, new_item)
        save_analyses_to_file(saved)
        
        # Also ensure Partner A is synced in saved_people.json; sync Partner B only if real person
        if data.get("p1") and data["p1"].get("name"):
            upsert_person_record(data["p1"])
        if analysis_type != "single_transit" and p2_name and "Current Sky" not in p2_name:
            upsert_person_record(p2_data)

        return jsonify({"success": True, "analysis": new_item}), 201
    except Exception as err:
        return jsonify({"error": str(err)}), 500

@app.route('/api/analyses/<analysis_id>', methods=['GET'])
def api_get_single_analysis(analysis_id):
    """Retrieve a single saved analysis."""
    saved = load_saved_analyses()
    item = next((x for x in saved if x["id"] == analysis_id), None)
    if not item:
        return jsonify({"error": "Analysis not found"}), 404
    return jsonify(item)

@app.route('/api/analyses/<analysis_id>', methods=['PUT'])
def api_update_analysis(analysis_id):
    """Update an existing analysis profile."""
    try:
        data = request.get_json(force=True)
        saved = load_saved_analyses()
        idx = next((i for i, x in enumerate(saved) if x["id"] == analysis_id), None)
        if idx is None:
            return jsonify({"error": "Analysis not found"}), 404
            
        item = saved[idx]
        if "title" in data: item["title"] = data["title"]
        if "p1" in data: item["p1"] = data["p1"]
        if "p2" in data: item["p2"] = data["p2"]
        if "notes" in data: item["notes"] = data["notes"]
        item["version"] = data.get("version") or item.get("version") or APP_VERSION
        item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        saved[idx] = item
        save_analyses_to_file(saved)
        return jsonify({"success": True, "analysis": item})
    except Exception as err:
        return jsonify({"error": str(err)}), 500

@app.route('/api/analyses/<analysis_id>', methods=['DELETE'])
def api_delete_analysis(analysis_id):
    """Delete a saved analysis profile."""
    try:
        saved = load_saved_analyses()
        initial_len = len(saved)
        saved = [x for x in saved if x["id"] != analysis_id]
        if len(saved) == initial_len:
            return jsonify({"error": "Analysis not found"}), 404
        save_analyses_to_file(saved)
        return jsonify({"success": True, "deleted_id": analysis_id})
    except Exception as err:
        return jsonify({"error": str(err)}), 500

# --- SAVED PEOPLE PROFILE ENDPOINTS ---
@app.route('/api/people', methods=['GET'])
def api_get_people():
    """List all saved individual person profiles."""
    return jsonify(load_saved_people())

@app.route('/api/people', methods=['POST'])
def api_save_person():
    """Save or update an individual person profile."""
    try:
        data = request.get_json(force=True)
        if not data or not data.get("name"):
            return jsonify({"error": "Name is required to save person profile"}), 400
        
        saved_record = upsert_person_record(data)
        return jsonify({"success": True, "person": saved_record}), 200
    except Exception as err:
        return jsonify({"error": str(err)}), 500

@app.route('/api/people/<person_id>', methods=['GET'])
def api_get_single_person(person_id):
    """Retrieve a single saved person profile."""
    people = load_saved_people()
    item = next((x for x in people if x["id"] == person_id), None)
    if not item:
        return jsonify({"error": "Person profile not found"}), 404
    return jsonify(item)

@app.route('/api/people/<person_id>', methods=['PUT'])
def api_update_person(person_id):
    """Update a saved person profile."""
    try:
        data = request.get_json(force=True)
        people = load_saved_people()
        idx = next((i for i, x in enumerate(people) if x["id"] == person_id), None)
        if idx is None:
            return jsonify({"error": "Person profile not found"}), 404
            
        item = people[idx]
        if "name" in data and data["name"]: item["name"] = data["name"].strip()
        if "date" in data: item["date"] = data["date"]
        if "time" in data: item["time"] = data["time"]
        if "city" in data: item["city"] = data["city"]
        if "tz" in data: item["tz"] = data["tz"]
        item["version"] = APP_VERSION
        item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        people[idx] = item
        save_people_to_file(people)
        return jsonify({"success": True, "person": item})
    except Exception as err:
        return jsonify({"error": str(err)}), 500

@app.route('/api/people/<person_id>', methods=['DELETE'])
def api_delete_person(person_id):
    """Delete a saved person profile."""
    try:
        people = load_saved_people()
        initial_len = len(people)
        people = [x for x in people if x["id"] != person_id]
        if len(people) == initial_len:
            return jsonify({"error": "Person profile not found"}), 404
        save_people_to_file(people)
        return jsonify({"success": True, "deleted_id": person_id})
    except Exception as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5050)