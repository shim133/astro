# Changelog

All notable changes to the **AstroMatch Pro** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
