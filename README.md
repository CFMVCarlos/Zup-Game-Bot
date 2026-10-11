# Zup! Game Bot

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Package Manager: uv](https://img.shields.io/badge/package%20manager-uv-de5fe9?logo=uv&logoColor=white)](https://astral.sh/uv)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-261230.svg?labelColor=grey&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Docstrings: NumPy](https://img.shields.io/badge/docstrings-numpy-4D77CF?logo=numpy&logoColor=white)](https://numpydoc.readthedocs.io/)
[![Type Checker: Basedpyright](https://img.shields.io/badge/type%20checker-basedpyright-informational?logo=python&logoColor=white)](https://github.com/detachhead/basedpyright)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Game: Zup! on Steam](https://img.shields.io/badge/Steam-Zup!-1b2838?logo=steam&logoColor=white)](https://store.steampowered.com/app/533300/Zup/)

**High-precision, resolution-adaptive automation bot for the puzzle game [Zup!](https://store.steampowered.com/app/533300/Zup/) on Steam.**

</div>

---

## 🎯 Overview

**Zup! Game Bot** automates gameplay across all 44 levels of *Zup!* by dispatching asynchronous, millimeter-accurate mouse clicks to detonate explosive blocks and guide the red sphere onto green platforms.

The bot features dynamic coordinate scaling from a reference 2560×1440 canvas to any target monitor resolution, pre-computed bounding-box RGB pixel polling for instantaneous level-completion detection, and keyboard hotkey orchestration.

---

## ✨ Features

- 🎮 **Complete Level Coverage**: Built-in sequence parameters for all 44 levels (`A`–`Z`, `0`–`9`, `<`, `>`, `#`, `!`, `@`, `$`, `~`, `*`).
- 📐 **Dynamic Coordinate Scaling**: Automatically scales reference 2560×1440 coordinates to the active monitor resolution.
- ⚡ **Optimized Pixel Polling**: Pre-computes bounding boxes for target checkout points, capturing only localized screen regions with Pillow for rapid RGB completion detection.
- 🔄 **Autonomous Level Retries**: Automatically detects failed states via configurable timeout thresholds and restarts the level.
- 🎯 **Coordinate Inspector**: Standalone `getMouse.py` calibration utility to sample and log real-time cursor coordinates on click.
- 🛡️ **Strict Quality Standards**: 100% typed with NumPy-style docstrings verified against `ruff`, `pydoclint`, `ty`, and `basedpyright`.

---

## ⌨️ Controls & Keybindings

| Keybinding | Action | Description |
| :--- | :--- | :--- |
| <kbd>Enter</kbd> | **Start Bot** | Initiates game startup and runs through the 44-level sequence |
| <kbd>Esc</kbd> | **Stop / Exit** | Gracefully cancels the active game task and terminates the bot |
| <kbd>Ctrl</kbd> + <kbd>C</kbd> | **Interrupt** | Halts the `getMouse.py` coordinate listener or running process |

---

## 🏗️ Project Architecture

```
Zup-Game-Bot/
├── common.py          # Screen scaling, async mouse clicks, and RGB pixel verification
├── Levels.py          # Data-driven LevelConfig definitions and level loop (1–44)
├── ZUP.py             # Main entry point with keyboard listener and task lifecycle
├── getMouse.py        # Calibration utility printing real-time cursor coordinates
├── pyproject.toml     # Project configuration, dependencies, and tool settings
├── requirements.txt   # Traditional pip dependency manifest
└── LICENSE            # MIT License
```

### Module Responsibilities

- **[`common.py`](file:///home/cfmv/projects/Zup-Game-Bot/common.py)**: Contains `convert_coords` for resolution mapping, `mouse_click` for left-click simulation, `checkOut` for localized pixel brightness sampling, `Reset` to trigger level resets, and `level_template_click` to coordinate multi-click level sequences with timeout retries.
- **[`Levels.py`](file:///home/cfmv/projects/Zup-Game-Bot/Levels.py)**: Houses the frozen dataclass `LevelConfig` and the comprehensive `LEVEL_CONFIGS` registry of all 44 levels with their precise timing delays and coordinate parameters.
- **[`ZUP.py`](file:///home/cfmv/projects/Zup-Game-Bot/ZUP.py)**: The primary application loop that listens for <kbd>Enter</kbd> to launch `run_game()` and <kbd>Esc</kbd> to exit.
- **[`getMouse.py`](file:///home/cfmv/projects/Zup-Game-Bot/getMouse.py)**: Event-driven mouse listener that outputs exact screen coordinates whenever the user clicks, enabling rapid calibration of new levels.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- Display environment (Windows, macOS, or X11 Linux)
- [uv](https://docs.astral.sh/uv/) (recommended) or standard `pip`

### Installation

#### Using `uv` (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/CFMVCarlos/Zup-Game-Bot.git
   cd Zup-Game-Bot
   ```

2. Synchronize dependencies into a managed virtual environment:
   ```bash
   uv sync
   ```

#### Using `pip`

```bash
git clone https://github.com/CFMVCarlos/Zup-Game-Bot.git
cd Zup-Game-Bot
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🕹️ Usage

### 1. Calibrate Screen Coordinates (Optional)

If adjusting level positions or verifying monitor scaling, run:

```bash
uv run python getMouse.py
# Or: python getMouse.py
```

Click anywhere on the screen to view the terminal coordinates. Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to exit.

### 2. Launch the Automation Bot

1. Open **Zup!** on Steam.
2. In your terminal, start the bot:
   ```bash
   uv run python ZUP.py
   # Or: python ZUP.py
   ```
3. Focus the game window and press <kbd>Enter</kbd> to begin.
4. Press <kbd>Esc</kbd> at any point to stop execution.

---

## 🧪 Code Quality & Verification

The codebase adheres to rigorous linting, formatting, docstring, and type-checking standards:

```bash
# Linting & Formatting
uv run ruff check
uv run ruff format --check

# NumPy Docstring Validation
uv run pydoclint .

# Fast Type Checking
uv run ty check

# Comprehensive Strict Type Checking
uv run basedpyright
```

---

## 📄 License

This project is open-source and distributed under the [MIT License](LICENSE).

---

## 👤 Author

Developed by **[Carlos Valente](https://github.com/CFMVCarlos)**.
Contributions, bug reports, and suggestions are welcome!