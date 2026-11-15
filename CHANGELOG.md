# Changelog

All notable changes to the **AstroMatch Pro** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.5.2] - 2026-11-15

### Added
- **Private Browser-Scoped Storage & Multi-User Isolation**:
  - All saved personal profiles and couple analyses are now isolated to the user's private browser `localStorage` (`astromatch_saved_people` & `astromatch_saved_analyses`).
  - Sharing the web link with others presents a clean, empty workspace: visitors cannot view any birthdays, names, or analyses entered by others.
  - Repository data stores (`saved_people.json` & `saved_analyses.json`) are completely sanitized to empty lists `[]`.
- **Data Backup & Restore Engine (Export / Import JSON)**:
  - **📥 Export Backup**: One-click download of all saved profiles and analyses as a portable JSON file (`astromatch_backup_YYYY-MM-DD.json`).
  - **📤 Import Backup**: One-click file picker that merges and restores saved people profiles and synastry analyses in seconds.
  - Automatically updates counts, filter badges, and form select dropdowns upon import.
  - Offline-first & future-proof: Prepares architecture for optional cross-device synchronization.
- **Privacy Indicator**:
  - Added subtle privacy badge in the Saved Database toolbar: `🔒 Personal Storage: Your data is stored privately in this browser only and is never visible to others`.

## [2.5.1] - 2026-11-05

### Added
- **Dedicated Single Entity & Daily Transit Alignment Mode (`is_single_entity`)**:
  - Automatically activates when Partner B is left blank or when analyzing a single entity alone (e.g., Elon Musk, SA, or YS).
  - Replaces romantic couple synastry with the **Cosmic Transit Resonance Index (מדד תהודת מעברים קוסמית לתאריך)**.
  - Computes 6 personalized daily transit influence metrics:
    - ⚡ **Active Transit Momentum** (`מומנטום מעברים פעיל`)
    - 💡 **Mental Focus & Clarity** (`מיקוד ובהירות מחשבתית`)
    - 🌊 **Emotional Grounding & Balance** (`איזון רגשי ורווחה אישית`)
    - 🏛️ **Resilience & Structural Discipline** (`יציבות ועמידות מול אתגרים`)
    - 🚀 **Executive Drive & Ambition** (`עוצמה ביצועית ושאפתנות`)
    - 💎 **Resource & Opportunity Flow** (`זרימת הזדמנויות ומשאבים`)
  - Partner B card dynamically transforms into the **Current Sky Planetary Positions Card (`🌍 מיקום כוכבי השמיים כיום`)** showing active transit degrees and a 1-click `➕ Compare Partner` action.
- **Interactive Help & Professional Astrological Guide (`❓ מדריך שימוש ואסטרולוגיה מקצועית`)**:
  - Added a dedicated, bilingual Help Modal accessible from the navbar and hero header in both `index.html` and `result.html`.
  - Comprehensive guide sections explaining Single Entity vs. Dual Synastry, why 98% compatibility appeared in previous versions, key chart axes (`Ascendant`, `Chart Ruler`, `Midheaven / MC`, `North Node`), Blind Portrait mode, and database snapshots.
- **Saved Analyses Filtering & Transit Snapshot Database**:
  - Added filter tabs in the Saved Analyses Manager: `🔘 All (הכל)`, `👤 Single & Transits (אישי ומעברים לתאריך)`, and `👥 Couples & Synastry (זוגות ושותפויות)`.
  - Distinguishes snapshots cleanly with dedicated visual badges (`👤 Single & Transits` vs `👥 Couple Synastry`).
  - Allows 1-click snapshot saving directly from both the calculator form and results page with smart auto-titling (`{Name} — Transit Snapshot ({Date})`).

### Fixed
- **Synastry Score Inflation Bug**:
  - Fixed the mathematical calculation in `_calculate_synastry_single` where unnormalized positive aspect points were unconditionally added to a base of 50, causing almost every pair (including individuals compared to the current sky) to score 88%-98%.
  - Replaced with a balanced **Harmonic-to-Tension Ratio** weighted by personal luminaries (`Sun`, `Moon`, `Venus`, `Mars`, `Ascendant`) vs generational outer planets (`Uranus`, `Neptune`, `Pluto`), producing realistic, nuanced scores (e.g., 65-75% for mixed pairs, 85-98% for rare harmonic alignment).
- **Single Entity Current Sky Fallback Bug**:
  - Fixed the issue where single entity submissions erroneously generated couple synastry and romantic compatibility ("Soulmate potential", "Romantic chemistry") with the sky of the current date.

## [2.5.0] - 2026-11-04

### Added
- **Expert Astrologist Synthesis Engine (`astro_expert.py`) — Bilingual (Hebrew & English)**:
  - **אופק (Ascendant / Rising Sign) & Chart Ruler (שליט המפה)**: Deep analysis of the Rising Sign degree, its traditional and modern planetary rulers, and the exact Sign and Natal House where the Chart Ruler is placed.
  - **Midheaven (רום שמיים - MC / 10th House) & MC Ruler**: Full analysis of the career/public destiny axis and its ruling planet's placement.
  - **Lunar North Node (ראש הדרקון ☊)**: Astronomical mean Lunar North Node calculation, house placement, and karmic trajectory synthesis.
  - **Apparent Retrograde Motion (`Rx`) & Essential Dignities**: Computes daily ecliptic speed (`deg/day`) to detect Retrograde motion (`Rx`) and evaluates Essential Dignities (`Domicile / שליט ביתו`, `Exaltation / נעלה`, `Detriment / ירוד`, `Fall / מפלה`, `Peregrine`).
  - **Geometric Patterns & Mutual Receptions**: Automatically detects Angular planets conjunct `ASC` or `MC`, Mutual Receptions (`קבלה הדדית`, e.g., Moon in Virgo ⇄ Mercury in Cancer), Stelliums, Focal Squares/T-Squares, and Oppositions channeled via a 3rd planet (Mystic Wedge).
  - **Elemental, Modal & Hemisphere Balance**: Computes weighted percentages across Fire/Earth/Air/Water, Cardinal/Fixed/Mutable, and Upper/Lower/Eastern/Western hemispheres.
  - **Complete Natal Aspects Catalog**: Interprets every internal aspect in the birth chart, including aspects to `Ascendant`, `Midheaven`, and `North Node`.
  - **🕵️ Blind Portrait & Blind Mode Toggle ("Who Is This Without Knowing Their Name?")**: Synthesizes a 4-part psychological, intellectual, material, and vocational portrait purely from the chart math without relying on the subject's name, plus a 1-click UI toggle (`🕵️ Blind Mode`) that masks names across the report.
- **Current Date Transits & Executive Forecast (`calculate_transits`)**:
  - Calculates real-time planetary positions for the current date/time (or any custom reference date) and maps them into Entity A's and Entity B's 12 Natal Houses and Transit-to-Natal aspects.
  - Added two interactive **Transits Bi-Wheel** modes (`🌍 Current Transits - Entity A` and `🌍 Current Transits - Entity B`) on the SVG wheel.
- **2-Entity Interaction & House Overlays (Person, Company, Organization, or Event)**:
  - Supports analyzing 2 People, a Person + Company (e.g., Founder & Corporation), 2 Companies, or a Single Entity against Current Sky Transits.
  - Computes **House Overlays (`השלכות בתים`)** showing how each entity's planets activate the other entity's 12 houses.
  - Added 2 new Synergy metrics (**6-Dimensional Synergy**): `⚡ Executive Power & Drive` and `💎 Wealth & Resource Flow`.
- **🧪 Elon Musk + SpaceX / Tesla Blind Verification Case Study**:
  - Pre-seeded verified birth/founding profiles for **Elon Musk** (`1971-06-28`, `07:30` SAST `+02:00`, `Pretoria, South Africa`), **SpaceX** (`2002-03-14`, `12:00`, `Hawthorne, USA`), and **Tesla, Inc.** (`2003-07-01`, `12:00`, `Palo Alto, USA`), plus a dedicated side-by-side verification tab comparing blind algorithmic chart deductions against documented reality.

## [2.4.1] - 2026-09-06

### Added
- **Dual Coordinate Systems Support (Tropical & J2000)**:
  - Added support for both **Tropical (Apparent Ecliptic of Date / Astro.com)** and **J2000 (Astrometric / Epoch J2000.0)** coordinate frameworks.
  - Interactive UI toggle button (`🌐 Tropical (Astro.com)` / `🔭 J2000 (Astrometric)`) in chart controls and data table header.
  - Dynamic client-side switching that instantly updates the SVG chart wheel, planetary degree glyphs, unequal house cusps, angular axes, aspect chords, data tables, aspect grid, compatibility score circle, and aspect interpretation cards.
  - Tropical coordinates use true ecliptic of date accounting for equinox precession, nutation, and light-time corrections, matching Astro.com and professional Swiss Ephemeris calculations to the exact arcminute.
  - Bilingual localization support (Hebrew & English) for coordinate system labels, descriptions, and tooltips.
- **Universal Standard Time (Non-DST) Notice & Consistency**:
  - Clarified and standardized time input across forms: times are entered in the location's standard astronomical GMT offset without daylight saving time (DST).
  - Added bilingual guidance notices (`tzStandardNotice`) on all timezone input fields and profile edit modals in both Hebrew and English.
  - Normalized all reference cities worldwide to standard non-DST offsets (e.g., standard GMT+2 for 30°-45°E, GMT-5 for NYC, GMT+0 for LON, GMT+1 for PAR).
  - Universal longitude-based geographic GMT offset estimation (`round(lon / 15.0)`) without any country-specific hardcoding.

## [2.4.0] - 2026-09-06

### Added
- **Professional Astrological Wheel Enhancements**:
  - Replaced standard equal house system with precise **Porphyry Unequal Houses**.
  - Dynamic SVG house sectors with calculated exact midpoints for labeling.
  - Angular axes explicitly labeled with exact degrees (`ASC`, `IC`, `DSC`, `MC`).
  - Added exact planetary degrees (0-29°) physically rendered next to each glyph on the wheel.
- **Synastry Aspect Matrix & Planetary Data Tables**:
  - Implemented a professional triangular/rectangular **Aspect Grid (Matrix)** displaying all calculated planetary aspects and orbs in the UI.
  - Added a responsive **Planetary Data Table** listing exact longitudes and house placements for all calculated bodies.

## [2.3.0] - 2026-09-06

### Added
- **Individual Person Profiles Repository (`saved_people.json`)**:
  - Independent persistent storage for individual astrological profiles (name, birth date, exact time/hour, city, and UTC timezone offset).
  - Seeded with initial profiles from existing records (`SA`, `YS`, `AM`, `Alex`, `Jordan`).
  - Full RESTful API in `app.py`: `GET /api/people`, `POST /api/people`, `PUT /api/people/<id>`, and `DELETE /api/people/<id>`.
  - Auto-sync integration: Saving a couple analysis now automatically registers and updates both partners in the person profile repository.

- **Independent Saved Person Selectors & Quick Swapping**:
  - Dedicated dropdown selector for Partner A and Partner B independently, enabling instant pairing of any saved person against any other partner.
  - Centered `🔄 Swap Partners (A ⇄ B)` 1-click button to flip Partner A and Partner B with all coordinates and timezone data preserved.

- **Live Saved Status Indicators & 1-Click Action Buttons**:
  - Real-time comparison between active form inputs and the person database.
  - Displays `✓ Saved` when details match.
  - Displays `Modified` and an immediate `💾 Update` button when details (e.g. birth hour) are edited.
  - Displays `Not saved` and a 1-click `💾 Save` button when entering a new person.

- **Interactive Results Page "Edit Details & Compare Partner" System**:
  - Top navigation and Partner Card `✏️ Edit Details / Compare Partner` button on `result.html`.
  - Opens a dedicated modal allowing instant adjustments to the hour of birth, switching Partner B to a different saved person, and recalculating via `⚡ Recalculate & Compare`.
  - Direct individual `💾 Save` / `✓ Saved` badges on the partner summary cards on the results page.

- **Dual-Tab Directory (Analyses & People Profiles)**:
  - Tabbed interface allowing users to manage both Couple Analyses and Individual People Profiles.
  - Person cards feature `👤 Set as Partner A`, `👤 Set as Partner B`, inline profile editing modal, and deletion.

- **Bilingual Localization Expansion**:
  - Full Hebrew and English translations for all new person selectors, status badges, modals, and comparison controls.

## [2.2.0] - 2026-09-06

### Added
- **Application Version Tracking System**:
  - Global `APP_VERSION = "2.2.0"` defined in `app.py` and provided to all frontend contexts.
  - **Saved Analyses Version Stamp**: Saving or updating couple profiles now stamps each profile record with the version number used (`"version": "2.2.0"`).
  - **Version Badge Display**: Saved analysis cards now prominently display their creation/update version badge (e.g., `v2.2.0`).
  - **Persistent Program Footers**: Clean, professional footer added to both the main calculation page and the synastry results page, displaying `AstroMatch Pro v2.2.0 · Pure NASA Ephemeris Engine · Built with Skyfield & Python`.

- **Multi-Language Engine (`static/translations.js`)**:
  - Full bilingual support starting with **Hebrew (`he`, RTL)** and **English (`en`, LTR)**.
  - Strict compliance with requested format:
    ```javascript
    export const TRANSLATIONS = {
      he: { dir: 'rtl', langName: 'עברית', appTitle: 'אסטרו-מאץ׳ פרו', ... },
      en: { dir: 'ltr', langName: 'English', appTitle: 'AstroMatch Pro', ... }
    };
    ```
  - Compatible with modern ES modules and direct browser scripts via global `window` exposure.
  - Dynamic page layout direction flipping (`document.documentElement.dir = 'rtl'` / `'ltr'`) and RTL-specific CSS enhancements.
  - Interactive language switcher toggle button (`🌐 עברית (HE) / 🌐 English (EN)`) in the top navigation bar of both pages.
  - Comprehensive localization across all layers:
    - Headers, subtitles, buttons, form inputs, placeholders, and tooltips.
    - Live geocoding status badges, confirmations, and alerts.
    - Astrological vocabulary: 12 Zodiac signs (טלה through דגים), 10 planets + ASC / MC, 5 major aspects (צמידות, טריין, סקסטיל, סקוויר, אופוזיציה), and the 4 elements.
    - Synastry category bars and compatibility rating verdicts.
    - Interactive SVG chart tooltips and chord hover descriptions.
  - Persistent user language preference saved in `localStorage` (`astromatch_lang`).

- **Expanded Israeli Cities & Regional Catalog**:
  - Added over 40 Israeli cities (including Ramat Gan, Kiryat Gat, Herzliya, Kfar Saba, Petah Tikva, Rishon LeZion, Ashdod, Netanya, Holon, Bnei Brak, Rehovot, Bat Yam, Givatayim, Hod HaSharon, Ramat HaSharon, Modi'in, Lod, Ramla, Ashkelon, Beit Shemesh, Nazareth, Tiberias, Nahariya, Acre, Afula, Hadera, Karmiel, Yavne, Kiryat Ono, Kiryat Motzkin, Kiryat Bialik, Kiryat Yam, Kiryat Ata, Dimona, Arad, Kiryat Shmona, Zikhron Ya'akov, Sderot, Netivot) with pre-verified coordinates and default offsets.

- **Transparent Live Geocoding Fallback & Source Reporting**:
  - Seamless fallback to live OpenStreetMap (Nominatim) lookup whenever a city is not in the curated database.
  - Explicit real-time UI status reporting indicating where the location is being queried from and whether it succeeded or needs a spelling check (`Searching OpenStreetMap...`, `Found via OpenStreetMap: Lat, Lon`, or `Not found - please check spelling`).
    - Fully bilingual status feedback integrated into the translation engine (Hebrew & English).

### Fixed
- **Partner Profile Card Degree & Position Rendering**:
  - Corrected degree and minute mapping (`sign_deg` and `sign_min` keys alongside `deg`/`min` in `compute_chart`) so planet position rows display exact coordinates (e.g., `1° 45' ☉ Pisces`) rather than missing degrees (`° 00'`).
  - Added robust fallback to pre-formatted coordinate strings when switching languages.
  - Streamlined Ascendant row labels (`ASC Rising` / `אופק (ASC)`) and applied `text-nowrap` to prevent awkward line breaks on high-density cards.

## [2.1.0] - 2026-09-06

### Added
- **Curated World Cities Catalog (`cities.json`)**:
  - Offline-capable database of over 120 major world cities and metropolitan regions across all continents.
  - Includes exact pre-verified latitudes, longitudes, canonical display names, and default UTC timezone offsets.
  - Searchable autocomplete dropdown (`<datalist>`) in city inputs with instant filtering.
  - Instant selection automatically locks in coordinates, auto-fills default UTC offset, and displays an interactive verification badge (`📍 Verified: Lat, Lon · Country`).
  - Fallback to live Nominatim geocoding for unlisted custom locations.
- **Saved Analyses Management System (Full CRUD)**:
  - Persistent JSON database storage (`saved_analyses.json`) preserving couple calculation profiles across restarts.
  - Complete REST API:
    - `GET /api/analyses`: list all saved profiles.
    - `POST /api/analyses`: save a new couple profile.
    - `GET /api/analyses/<id>`: retrieve individual profile.
    - `PUT /api/analyses/<id>`: update/edit saved couple data.
    - `DELETE /api/analyses/<id>`: remove profile from storage.
  - Interactive UI Management Panel on homepage:
    - Searchable list of saved couple profiles.
    - **Load into Form**: Populates form inputs with a single click.
    - **Inline Edit Modal**: Allows editing names, dates, times, cities, timezones, and notes.
    - **Delete**: Instant removal with confirmation dialog.
  - **Quick Save Actions**:
    - "💾 Save to My Analyses" button directly on the homepage input form.
    - "💾 Save to My Analyses" button in the result report action bar.

## [2.0.0] - 2026-09-06

### Added
- **Visual Astrological Maps (Interactive SVG Engine)**:
  - **Synastry Bi-Wheel Mode**: Concentric circular chart with Partner A's planets on the inner ring, Partner B's planets on the outer ring, and inter-chart aspect chords in the center.
  - **Individual Natal Chart Modes**: Standalone single-wheel natal charts for Partner A and Partner B with 12 house sectors and natal aspect lines.
  - **12 Zodiac Segments**: Elemental color-coding (Fire, Earth, Air, Water), traditional astrological glyphs (♈ through ♓), and 5° / 10° degree tick marks.
  - **Ascendant Orientation**: Standard eastern horizon orientation (Ascendant at 9 o'clock / 180°), with degrees advancing counterclockwise.
  - **Aspect Chords Web**: Center aspect lines connecting cross-chart planetary positions, color-coded by nature:
    - Trine (120°): Emerald Green (`#10b981`)
    - Sextile (60°): Electric Cyan (`#06b6d4`)
    - Conjunction (0°): Radiant Gold (`#fbbf24`)
    - Square (90°): Fiery Crimson (`#ef4444`)
    - Opposition (180°): Ruby Rose (`#f43f5e`)
  - **Orb Tightness Scaling**: Dynamic line weight and opacity based on orb tightness (tighter orbs appear bolder and brighter).
  - **Anti-Collision Layout**: Intelligent radial staggering algorithm preventing glyph overlaps for tight conjunctions.
  - **Interactive Inspecting**: Hovering over planets displays exact degrees, minutes, sign, house, and highlights associated aspect lines; hovering over chords reveals the aspect angle, orb, and astrological interpretation.
  - **Chart Export**: Direct one-click download buttons for **SVG** and high-resolution **PNG** (1800x1800).
  - **Aspect Filters**: Interactive buttons on the map to filter visible chords by aspect type (All, Trines, Sextiles, Conjunctions, Squares, Oppositions).

- **Celestial Math & Expanded Planetary Roster**:
  - Added outer planets: **Jupiter**, **Saturn**, **Uranus**, **Neptune**, and **Pluto** via pure-Python Skyfield barycenter calculations (`de421.bsp`).
  - Added celestial angle calculations: **Ascendant ($ASC$)**, **Midheaven ($MC$)**, **Descendant ($DSC$)**, and **Imum Coeli ($IC$)** from Local Sidereal Time ($LST$) and Earth obliquity.
  - Added **12 Equal House Cusps** calculation and automated house placement mapping for each planetary body.
  - Added natal aspect calculations for individual charts.

- **Compatibility Scoring & Aspect Catalog**:
  - Categorized score breakdown:
    - Overall Synastry Score (0–100% normalized index)
    - Romantic & Physical Chemistry (Venus/Mars/Sun-Moon)
    - Emotional Safety & Depth (Moon/Neptune)
    - Intellectual & Conversational Spark (Mercury/Uranus)
    - Long-Term Stability & Commitment (Saturn/Jupiter/Angles)
  - Detailed aspect interpretation matrix covering classical archetype pairings with filterable cards (All, Harmonious, Dynamic Friction).

- **User Interface & Styling**:
  - Celestial glassmorphism design with Google Fonts (`Cinzel` and `Outfit`).
  - Timezone helper pills for quick offset selection (TLV, NYC, LON, PAR, LAX).
  - 1-click sample couple loader ("Alex & Jordan") for rapid testing and demonstrations.
  - Port configured to `5050` to avoid conflicts with other local dev servers.

- **Environment & IDE Integration**:
  - Conda environment configuration targeting `D:\Resources\Anaconda3\envs\astromatch` (Python 3.11).
  - Permanent VS Code / Antigravity IDE configuration via `.vscode/settings.json`, `.vscode/launch.json`, and `.vscode/tasks.json`.
  - Workspace agent rule `.agents/rules/astromatch-environment.md` for consistent automated interpreter binding across restarts.
  - Exported `environment.yml` for exact environment reproduction.
  - `.gitignore` configured for Python, IDE, and OS artifacts.

---

## [1.0.0] - Prior Initial Prototype
- Initial Flask proof-of-concept calculating basic Big Three (Sun, Moon, Ascendant) and inner planets (Mercury, Venus, Mars) using Skyfield and NASA `de421.bsp`.
- Basic text-based synastry scoring and Bootstrap form.
