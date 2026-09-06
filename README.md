# AstroMatch Pro (v2.0.0)

Professional-grade Astrological Compatibility (Synastry) & Interactive Celestial Maps web application.

AstroMatch Pro calculates the precise astronomical positions of planets for two individuals based on their exact birth date, time, timezone offset, and city. It computes celestial angles, 12 house cusps, geometric aspect chords between charts, and visualizes them on interactive Astrological Maps (Synastry Bi-Wheel and Natal Charts).

---

## Key Features

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
  - 12 Equal House Cusps with automatic house assignment for each body.

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
├── templates/
│   ├── index.html                     # Celestial input form & sample loader
│   └── result.html                    # SVG Astrological Map & aspect matrix
├── .gitignore                         # Git ignore configuration
├── app.py                             # Core Flask backend & celestial math engine
├── CHANGELOG.md                       # Semantic version history (v2.0.0)
├── de421.bsp                          # NASA JPL planetary ephemeris (~16 MB)
├── environment.yml                    # Conda environment specification
└── README.md                          # Project documentation
```