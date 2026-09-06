# AstroMatch Environment Configuration

## Python Environment
- **Conda environment path**: `D:\Resources\Anaconda3\envs\astromatch`
- **Conda environment name**: `astromatch`
- **Python interpreter**: `D:\Resources\Anaconda3\envs\astromatch\python.exe`
- **Python version**: 3.11

## Running the Application
- Always activate the environment before running: `conda activate astromatch`
- Or use the full interpreter path: `D:\Resources\Anaconda3\envs\astromatch\python.exe app.py`
- The Flask dev server runs on `http://127.0.0.1:5050`

## Key Dependencies
- `flask` — Web framework
- `skyfield` — Pure-Python astronomy library (no C extensions needed)
- `numpy` — Numerical computations
- `geopy` — Geocoding city names to lat/lon coordinates
- NASA ephemeris file `de421.bsp` is already included in the project root

## Technical Constraints
- **No C++ compiler available** — Do not use `pyswisseph`, `kerykeion`, `flatlib`, or any library requiring C extensions.
- All astrological math (zodiac signs, ascendant, aspects, orbs) is implemented manually in Python.
- Skyfield is used purely for astronomical planet positions.
