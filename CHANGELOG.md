# Changelog

All notable changes to the **AstroMatch Pro** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
