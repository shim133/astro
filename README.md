# AstroMatch Pro (v2.4.1)

Professional-grade Astrological Compatibility (Synastry) & Interactive Celestial Maps web application.

AstroMatch Pro calculates the precise astronomical positions of planets for two individuals based on their exact birth date, time, timezone offset, and city. It computes celestial angles, 12 house cusps, geometric aspect chords between charts, and visualizes them on interactive Astrological Maps (Synastry Bi-Wheel and Natal Charts).

---

## Key Features

- **Dual Coordinate Systems with Interactive Toggle (New in v2.4.1)**:
  - **Tropical (Date / Astro.com)**: Western astrology standard based on the apparent ecliptic of date, accounting for equinox precession, nutation, and light-time corrections. Matches Astro.com and Swiss Ephemeris calculations to the exact arcminute.
  - **J2000 (Astrometric)**: Modern astrophysical coordinate system fixed to the standard epoch J2000.0 without date precession.
  - **Instant UI Switch Button**: Toggle seamlessly between `🌐 Tropical (Astro.com)` and `🔭 J2000 (Astrometric)` on the chart toolbar and data tables without page reloads.
  - All visual elements (SVG chart wheel, planetary degree glyphs, house cusps, aspect grid, compatibility scores, and aspect catalog) dynamically update in real time.

- **Professional Astrological Charts (v2.4.0)**:
  - **Porphyry Unequal Houses**: Transitioned from equal houses to precise Porphyry unequal houses with dynamic visual SVG sectors and centered Roman numerals.
  - **Exact Degrees on Wheel**: Explicitly rendered degree values (0-29°) next to each planetary glyph on the chart.
  - **Distinct Angular Axes**: Distinctly labeled ASC, IC, DSC, and MC with their exact calculated degrees on the SVG wheel.
  - **Aspect Grid (Matrix)**: Triangular (Natal) and Rectangular (Synastry) Aspect Grid tables rendering full aspect and exact orb data.
  - **Planetary Data Tables**: Tabular display of precise planetary longitude (Sign, Degree, Minute) and house placement alongside the chart.

- **Individual Person Profiles & Partner Comparison System (New in v2.3.0)**:
  - **Saved People Directory (`saved_people.json`)**: Save individual birth profiles (birth date, exact hour of birth, city, timezone) for rapid pairing.
  - **Independent Partner Selectors**: Select any saved individual for Partner A and Partner B independently to quickly compare against multiple partners.
  - **Live Save Status Indicators**: Real-time comparison between entered details and saved records (`✓ Saved`, `Modified 💾 Update`, or `Not saved 💾 Save`).
  - **Interactive Results Page Comparison Modal**: Easily adjust the hour of birth or switch partners directly from the results view and recalculate instantaneously.
  - **1-Click Partner Swap**: Instantly flip Partner A and Partner B with coordinates and parameters preserved.
  - **Dual-Tab Directory**: Tabbed manager on the main page for both Saved Couple Analyses and Individual People Profiles.

- **Multi-Language Architecture (Hebrew & English)**:
  - Built-in bilingual support with instant language switching (`🌐 עברית / English`).
  - Automatic RTL (Right-to-Left) and LTR layout adaptation.
  - Centralized dictionary in `static/translations.js` exporting `TRANSLATIONS` for both ES modules and browser scripts.
  - Complete coverage: UI forms, badges, modals, tooltips, astrological terms, and compatibility verdicts.
  - User preference persisted across visits in `localStorage`.

- **Version Tracking & Metadata Display**:
  - Global `APP_VERSION = "2.4.1"` in `app.py`.
  - All saved analyses and people profiles are stamped with the version number used (`"version": "2.4.1"`).
  - Saved cards display a version badge (e.g. `v2.3.0`).
  - Persistent application footer displayed below the program on all screens.

- **Curated World Cities & Verification**:
  - Pre-verified catalog of 120+ global cities across all continents with exact latitudes, longitudes, and default UTC offsets.
  - Searchable autocomplete dropdown (`<datalist>`) for selecting birth cities.
  - Selecting a city locks in verified coordinates, auto-fills the timezone offset, and displays an instant verification badge (`📍 Verified: Lat, Lon · Country`).
  - Fallback to live geocoding for unlisted custom locations.

- **Saved Analyses Management (Full CRUD)**:
  - Persistent JSON database storage (`saved_analyses.json`) so your couple profiles are saved across sessions.
  - Dedicated manager on the homepage:
    - **List & Search**: Browse all saved couples with metadata and birth details.
    - **Load into Form**: Populate both partners' details with one click.
    - **Inline Edit**: Edit names, birth dates, times, cities, or notes in a clean modal dialog.
    - **Delete**: Remove profiles with instant UI update.
  - Quick-save buttons on both the homepage form and the result report header.

- **Interactive Astrological Maps (Pure SVG Engine)**:
  - **Synastry Bi-Wheel**: Partner A on the inner track, Partner B on the outer track, with color-coded inter-chart aspect chords in the center.
  - **Individual Natal Charts**: Standalone chart wheels for Partner A and Partner B with 12 house sectors (Roman numerals I–XII) and natal aspect lines.
  - **12 Zodiac Segments**: Elemental color-coding (Fire, Earth, Air, Water), traditional astrological glyphs (♈ to ♓), and 5° / 10° degree ticks.
  - **Ascendant Alignment**: Eastern horizon orientation (Ascendant at 9 o'clock / 180°), with longitudes advancing counterclockwise.
  - **Dynamic Aspect Chords**: Color-coded geometric chords (Trines in green, Sextiles in cyan, Conjunctions in gold, Squares in crimson, Oppositions in ruby) with line weight and opacity tied to orb tightness.
  - **Anti-Collision Layout**: Intelligent radial staggering prevents overlapping glyphs during tight conjunctions.
  - **Interactive Hover**: Hovering over planets or aspect lines displays exact degrees, houses, and rich interpretations.
  - **High-Resolution Export**: One-click **Export SVG** and **Export PNG** (1800×1800) buttons.

- **Expanded Planetary Roster & House Mathematics**:
  - Full 10-body roster: Sun (☉), Moon (☽), Mercury (☿), Venus (♀), Mars (♂), Jupiter (♃), Saturn (♄), Uranus (♅), Neptune (♆), Pluto (♇).
  - Angles: Ascendant ($ASC$), Midheaven ($MC$), Descendant ($DSC$), Imum Coeli ($IC$).
  - 12 Porphyry Unequal House Cusps with automatic house assignment for each body.

- **Compatibility Breakdown**:
  - Overall Synastry Score (0–100%) with cosmic verdict.
  - Categorized breakdown: Romantic Chemistry, Emotional Safety, Mental Rapport, Long-Term Stability.
  - Filterable aspect catalog (All, Harmonious, Dynamic Friction).

- **Strict "No C++ Compiler" Design**:
  - Built with pure Python astronomy tools (`skyfield`) and NASA's `de421.bsp` ephemeris.
  - Zero reliance on C-extensions or compiled packages like `pyswisseph`, `kerykeion`, or `flatlib`.

---

## Environment Setup & Quick Start

### 1. Conda Environment
The environment is configured at `D:\Resources\Anaconda3\envs\astromatch`:

```powershell
# Activate the environment
conda activate astromatch

# Or activate by prefix
conda activate D:\Resources\Anaconda3\envs\astromatch
```

To recreate the environment on a new computer:
```powershell
conda env create -f environment.yml
```

### 2. Running the Application
```powershell
# Directly with the environment's python interpreter
& "D:\Resources\Anaconda3\envs\astromatch\python.exe" app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5050`**

### 3. IDE Integration (Antigravity & VS Code)
- `.vscode/settings.json` is preconfigured with `python.defaultInterpreterPath` pointing directly to the `astromatch` interpreter.
- `.vscode/launch.json` provides a one-click debug launcher (`F5`).
- `.vscode/tasks.json` provides a default build/run task.
- `.agents/rules/astromatch-environment.md` instructs Antigravity to always use this isolated environment.

---

## Project Structure

```text
astroDating/
├── .agents/
│   └── rules/
│       └── astromatch-environment.md  # Workspace rules for Antigravity
├── .vscode/
│   ├── launch.json                    # Flask debug launch config
│   ├── settings.json                  # Python interpreter binding
│   └── tasks.json                     # Task runner configuration
├── static/
│   └── translations.js                # Bilingual translation engine (HE/EN) & RTL controller
├── templates/
│   ├── index.html                     # Celestial form, city search & saved analyses manager
│   └── result.html                    # SVG Astrological Map & aspect matrix
├── .gitignore                         # Git ignore configuration
├── app.py                             # Core Flask backend & celestial math engine (v2.4.0)
├── CHANGELOG.md                       # Semantic version history (v2.4.0)
├── cities.json                        # Curated database of world cities & coordinates
├── de421.bsp                          # NASA JPL planetary ephemeris (~16 MB)
├── environment.yml                    # Conda environment specification
├── README.md                          # Project documentation
└── saved_analyses.json                # Persistent JSON database for couple profiles
```