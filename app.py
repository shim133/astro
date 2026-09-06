from flask import Flask, render_template, request, jsonify
from skyfield.api import load
import numpy as np
from datetime import datetime
from geopy.geocoders import Nominatim
import ssl
import json

import os
import uuid

app = Flask(__name__)

APP_VERSION = "2.2.0"

# --- FILE PATHS & DATA LOADING ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CITIES_FILE = os.path.join(BASE_DIR, 'cities.json')
SAVED_ANALYSES_FILE = os.path.join(BASE_DIR, 'saved_analyses.json')

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

def load_saved_analyses():
    if not os.path.exists(SAVED_ANALYSES_FILE):
        return []
    try:
        with open(SAVED_ANALYSES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as err:
        print(f"Error reading {SAVED_ANALYSES_FILE}: {err}")
        return []

def save_analyses_to_file(data):
    with open(SAVED_ANALYSES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# --- CONFIG & EPHEMERIS LOADING ---
# Fix SSL for geopy
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

geolocator = Nominatim(user_agent="astro_match_pro_v3", ssl_context=ctx)

# Load NASA Ephemeris
print("Loading NASA Ephemeris data (de421.bsp)...")
eph = load('de421.bsp')
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

def calculate_angles_and_houses(t, lat, lon):
    """
    Calculate Ascendant, Midheaven (MC), Descendant, Imum Coeli (IC),
    and 12 Equal House Cusps.
    """
    gast_hours = t.gast
    lst_hours = (gast_hours + lon / 15.0) % 24
    ramc_deg = (lst_hours * 15.0) % 360
    eps_rad = np.radians(23.4392911) # Obliquity of Ecliptic
    
    ramc_rad = np.radians(ramc_deg)
    lat_rad = np.radians(lat)
    
    # Ascendant
    num = -np.cos(ramc_rad)
    den = (np.sin(ramc_rad) * np.cos(eps_rad)) + (np.tan(lat_rad) * np.sin(eps_rad))
    asc_deg = float(np.degrees(np.arctan2(num, den)) % 360)
    
    # Midheaven (MC)
    mc_deg = float(np.degrees(np.arctan2(np.sin(ramc_rad), np.cos(ramc_rad) * np.cos(eps_rad))) % 360)
    
    # Descendant and IC
    dsc_deg = float((asc_deg + 180) % 360)
    ic_deg = float((mc_deg + 180) % 360)
    
    # 12 Equal Houses (House 1 starts at ASC)
    houses = []
    for h in range(12):
        cusp = (asc_deg + h * 30.0) % 360
        houses.append({
            "house": h + 1,
            "cusp": round(float(cusp), 2),
            "zodiac": format_zodiac(cusp)
        })
        
    return {
        "asc": asc_deg,
        "mc": mc_deg,
        "dsc": dsc_deg,
        "ic": ic_deg,
        "houses": houses
    }

def get_house_for_lon(lon_deg, asc_deg):
    """Determine which equal house (1-12) an ecliptic longitude falls into."""
    diff = (lon_deg - asc_deg) % 360
    return int(diff // 30) + 1

def compute_chart(name, date_str, time_str, tz_str, city_str):
    """Calculates all planetary coordinates, angles, houses, and natal aspects."""
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
    
    # Calculate celestial angles & houses
    angles = calculate_angles_and_houses(t, lat, lon)
    asc_deg = angles["asc"]
    
    # Calculate all planets
    planets_list = []
    planets_dict = {}
    
    for p_name, p_info in PLANETS_CONFIG.items():
        p_obj = eph[p_info['target']]
        astrometric = earth.at(t).observe(p_obj)
        _, lon_ecl, _ = astrometric.ecliptic_latlon()
        deg = float(lon_ecl.degrees % 360)
        
        zodiac = format_zodiac(deg)
        house_num = get_house_for_lon(deg, asc_deg)
        
        planet_entry = {
            "name": p_name,
            "symbol": p_info["symbol"],
            "color": p_info["color"],
            "category": p_info["category"],
            "lon": round(deg, 2),
            "sign": zodiac["sign"],
            "sign_symbol": zodiac["symbol"],
            "sign_deg": zodiac["deg"],
            "sign_min": zodiac["min"],
            "deg": zodiac["deg"],
            "min": zodiac["min"],
            "sign_color": zodiac["color"],
            "formatted": zodiac["formatted"],
            "house": house_num
        }
        planets_list.append(planet_entry)
        planets_dict[p_name] = planet_entry

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
        "sign_deg": mc_zodiac["deg"],
        "sign_min": mc_zodiac["min"],
        "deg": mc_zodiac["deg"],
        "min": mc_zodiac["min"],
        "sign_color": mc_zodiac["color"],
        "formatted": mc_zodiac["formatted"],
        "house": get_house_for_lon(angles["mc"], asc_deg)
    }

    # Natal aspects for this individual
    all_points = planets_list + [asc_entry]
    natal_aspects = []
    for i in range(len(all_points)):
        for j in range(i + 1, len(all_points)):
            pt1 = all_points[i]
            pt2 = all_points[j]
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
        "asc": round(asc_deg, 2),
        "mc": round(angles["mc"], 2),
        "dsc": round(angles["dsc"], 2),
        "ic": round(angles["ic"], 2),
        "houses": angles["houses"],
        "planets": planets_list,
        "planets_dict": planets_dict,
        "asc_point": asc_entry,
        "mc_point": mc_entry,
        "natal_aspects": natal_aspects,
        # Big Three shorthand
        "sun_sign": planets_dict["Sun"]["sign"],
        "moon_sign": planets_dict["Moon"]["sign"],
        "asc_sign": asc_zodiac["sign"],
    }

def calculate_synastry(c1, c2):
    """Calculates all inter-chart aspects, compatibility score breakdown, and interpretations."""
    aspects = []
    
    # Points to compare
    pts1 = c1["planets"] + [c1["asc_point"]]
    pts2 = c2["planets"] + [c2["asc_point"]]
    
    raw_score = 0.0
    category_scores = {
        "chemistry": 50.0,
        "emotional": 50.0,
        "intellectual": 50.0,
        "stability": 50.0
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
                    
                    # Point calculation
                    weight = PLANETS_CONFIG.get(p1['name'], {}).get('weight', 1.0) * \
                             PLANETS_CONFIG.get(p2['name'], {}).get('weight', 1.0)
                    pt = asp_cfg["base_points"] * tightness * weight
                    raw_score += pt
                    
                    # Categorized impact
                    pair_names = {p1['name'], p2['name']}
                    if pair_names & {'Venus', 'Mars'}:
                        category_scores["chemistry"] += pt * 1.5
                    if pair_names & {'Moon', 'Neptune', 'Sun'}:
                        category_scores["emotional"] += pt * 1.3
                    if pair_names & {'Mercury', 'Uranus'}:
                        category_scores["intellectual"] += pt * 1.4
                    if pair_names & {'Saturn', 'Jupiter', 'Ascendant'}:
                        category_scores["stability"] += pt * 1.3
                    
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
    
    # Normalize scores between 20 and 99%
    def clamp_score(val):
        return int(max(25, min(98, round(val))))
        
    overall_pct = clamp_score(50 + (raw_score * 0.9))
    chemistry_pct = clamp_score(category_scores["chemistry"])
    emotional_pct = clamp_score(category_scores["emotional"])
    intellectual_pct = clamp_score(category_scores["intellectual"])
    stability_pct = clamp_score(category_scores["stability"])
    
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

    return {
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

# --- ROUTES ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_version=APP_VERSION)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        p1_inputs = {
            'name': request.form['p1_name'].strip(),
            'date_str': request.form['p1_date'],
            'time_str': request.form['p1_time'],
            'city_str': request.form['p1_city'].strip(),
            'tz_str': request.form['p1_tz'].strip()
        }
        p2_inputs = {
            'name': request.form['p2_name'].strip(),
            'date_str': request.form['p2_date'],
            'time_str': request.form['p2_time'],
            'city_str': request.form['p2_city'].strip(),
            'tz_str': request.form['p2_tz'].strip()
        }
        
        # Calculate individual charts
        chart1 = compute_chart(**p1_inputs)
        chart2 = compute_chart(**p2_inputs)
        
        # Calculate Synastry
        synastry = calculate_synastry(chart1, chart2)
        
        # Bundle everything for frontend visualization
        payload = {
            "chart1": chart1,
            "chart2": chart2,
            "synastry": synastry,
            "zodiac_data": ZODIAC_DATA
        }
        
        return render_template(
            'result.html',
            p1=chart1,
            p2=chart2,
            synastry=synastry,
            payload_json=json.dumps(payload),
            app_version=APP_VERSION
        )
        
    except Exception as e:
        import traceback
        return render_template(
            'index.html',
            error=f"Error calculating charts: {str(e)}",
            app_version=APP_VERSION
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
            
            # Smart timezone estimation
            if "ישראל" in addr or "Israel" in addr or (29.5 <= lat <= 33.5 and 34.0 <= lon <= 36.0):
                tz_est = "+03:00"
            else:
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
        new_item = {
            "id": f"match-{analysis_id}",
            "title": data.get("title") or f"{data.get('p1', {}).get('name', 'Partner A')} & {data.get('p2', {}).get('name', 'Partner B')}",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "version": data.get("version") or APP_VERSION,
            "p1": data.get("p1", {}),
            "p2": data.get("p2", {}),
            "notes": data.get("notes", "")
        }
        saved.insert(0, new_item)
        save_analyses_to_file(saved)
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

if __name__ == '__main__':
    app.run(debug=True, port=5050)