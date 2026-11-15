# AstroMatch Pro (v2.5.1)

Professional-grade Astrological Compatibility (Synastry), Single-Entity Transit Alignment & Cosmic Resonance, Expert Natal Dossier, and Interactive Celestial Maps web application.

AstroMatch Pro calculates the precise astronomical positions of planets, lunar nodes, and cardinal angles for single individuals, couples, or entities (people, companies, organizations, or historical events) as well as real-time **Current Date Transits**. It computes unequal Porphyry house cusps, Essential Dignities, Retrograde motion (`Rx`), Mutual Receptions, House Overlays, and Blind Astrological Portraits, visualizing them on interactive SVG Astrological Maps (Synastry Bi-Wheel, Natal Charts, and Current Transits Bi-Wheels).

---

## Key Features

- **Single Entity & Daily Transit Alignment Mode (New in v2.5.1)**:
  - **No Need to Always Enter a Second Entity**: Analyze a single person or company alone against current (or custom date) planetary transits.
  - **Cosmic Transit Resonance Index (`מדד תהודת מעברים קוסמית`)**: Replaces romantic couple compatibility with 6 individual transit influence areas: Active Transit Momentum, Mental Focus & Clarity, Emotional Grounding, Resilience & Structural Discipline, Executive Drive & Ambition, and Resource & Opportunity Flow.
  - **Real-Time Sky Card**: Automatically displays the current planetary sky positions with a 1-click option to add or compare a partner.

- **Balanced Synastry Scoring Engine (New in v2.5.1)**:
  - **Non-Inflated, Realistic Compatibility Rating**: Eliminates score inflation by evaluating the weighted ratio of harmonious aspects (trines, sextiles, favorable conjunctions) versus challenging friction (squares, oppositions).
  - **Personal Luminary Prioritization**: Personal points (`Sun`, `Moon`, `Venus`, `Mars`, `Ascendant`) carry high weight (1.4x-1.5x), while generational outer planets (`Uranus`, `Neptune`, `Pluto`) carry lower weight (0.5x).

- **Interactive Help & Astrological Guide Modal (`❓ מדריך שימוש ואסטרולוגיה מקצועית`) (New in v2.5.1)**:
  - Bilingual popup modal accessible from both the homepage and results view.
  - In-depth, accessible explanations of Single Entity vs. Dual Synastry, why 98% compatibility appeared in previous versions, key chart axes (`Ascendant`, `Chart Ruler`, `Midheaven / MC`, `North Node`), Blind Portrait mode, and database snapshots.

- **Saved Analyses Filtering & Transit Snapshot Database (New in v2.5.1)**:
  - Avoids clutter with category filter pills in the Saved Analyses Manager: `🔘 All`, `👤 Single & Transits`, and `👥 Pairs & Synastry`.
  - 1-click snapshot saving directly from both calculator forms and results pages, auto-tagged with transit date/time.

- **Expert Astrologist Engine & Blind Portrait Synthesis (v2.5.0)**:
  - **אופק (Ascendant / Rising Sign) & Chart Ruler (שליט המפה)**: Deep analysis of the Rising Sign degree, its planetary ruler, and the house/sign where the Chart Ruler steers the life trajectory.
  - **Midheaven (רום שמיים - MC) & MC Ruler + Lunar North Node (ראש הדרקון ☊)**: Complete vocational and karmic destiny analysis.
  - **Retrograde (`Rx`), Daily Speed & Essential Dignities**: Full evaluation of apparent retrograde motion and planetary dignity (`Domicile`, `Exaltation`, `Detriment`, `Fall`, `Peregrine`).
  - **Geometric Patterns & Mutual Receptions**: Automatic detection of angular planets conjunct `ASC`/`MC`, Mutual Receptions (`קבלה הדדית`), Stelliums, Focal Squares, and Channeled Oppositions (Wedges).
  - **🕵️ Blind Portrait & Blind Mode Toggle**: Deduces who a person or entity is strictly from their chart geometry without using their name, with a 1-click **Blind Mode** toggle on the report page.
  - **🌍 Current Date Transits & Transits Bi-Wheel**: Computes planetary positions for today (or any chosen date), maps them onto each entity's 12 natal houses and natal planets, and renders an interactive **Transits Bi-Wheel** on the SVG map.
  - **🤝 2-Entity Interaction (People, Companies, Events) & House Overlays**: Analyzes Person + Person, Founder + Company, or Company + Company with full **House Overlays (`השלכות בתים`)** and **6-Dimensional Synergy Scores** (adding `Executive Power & Drive` and `Wealth & Resource Flow`).
  - **🧪 Elon Musk Blind Verification Case Study**: Built-in 1-click benchmark (`1971-06-28 07:30 Pretoria` + `SpaceX` / `Tesla`) comparing blind astrological deductions against documented reality.

- **Dual Coordinate Systems with Interactive Toggle (v2.4.1)**:
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