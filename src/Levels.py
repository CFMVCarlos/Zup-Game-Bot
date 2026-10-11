"""Level sequences and automation coordinates for Zup!.

This module defines the coordinate configurations, timing delays, and execution
routines for all 44 levels of Zup!. Each level configuration maps to precise
click positions scaled to the user's active screen display.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from src.common import level_template_click


@dataclass(frozen=True)
class LevelConfig:
    """Configuration for an individual level click sequence.

    Attributes
    ----------
    level_number : int
        Sequential level number (1 through 44).
    label : str
        Level achievement character or label (e.g., 'A', '1', '*').
    x1 : int
        Primary click horizontal coordinate.
    y1 : int
        Primary click vertical coordinate.
    x2 : int | None
        Secondary click horizontal coordinate, by default None.
    y2 : int | None
        Secondary click vertical coordinate, by default None.
    x3 : int | None
        Tertiary click horizontal coordinate, by default None.
    y3 : int | None
        Tertiary click vertical coordinate, by default None.
    delay1 : float | None
        Delay before primary click in seconds, by default None.
    delay2 : float | None
        Delay before secondary click in seconds, by default None.
    delay3 : float | None
        Delay before tertiary click in seconds, by default None.
    reset_time : float
        Timeout limit before resetting in seconds, by default 5.0.
    """

    level_number: int
    label: str
    x1: int
    y1: int
    x2: int | None = None
    y2: int | None = None
    x3: int | None = None
    y3: int | None = None
    delay1: float | None = None
    delay2: float | None = None
    delay3: float | None = None
    reset_time: float = 5.0


LEVEL_CONFIGS: Final[tuple[LevelConfig, ...]] = (
    # Letters A through Z (Levels 1 to 26)
    LevelConfig(level_number=1, label="A", x1=1303, y1=800),
    LevelConfig(level_number=2, label="B", x1=1245, y1=800),
    LevelConfig(level_number=3, label="C", x1=1245, y1=800),
    LevelConfig(level_number=4, label="D", x1=1245, y1=800),
    LevelConfig(level_number=5, label="E", x1=1234, y1=760),
    LevelConfig(level_number=6, label="F", x1=1410, y1=803),
    LevelConfig(level_number=7, label="G", x1=1232, y1=808),
    LevelConfig(level_number=8, label="H", x1=1159, y1=802),
    LevelConfig(level_number=9, label="I", x1=1276, y1=556, delay1=0.5),
    LevelConfig(level_number=10, label="J", x1=1186, y1=591),
    LevelConfig(level_number=11, label="K", x1=1232, y1=764),
    LevelConfig(level_number=12, label="L", x1=1359, y1=716, delay1=0.65),
    LevelConfig(level_number=13, label="M", x1=1361, y1=636, delay1=0.5),
    LevelConfig(level_number=14, label="N", x1=1269, y1=678),
    LevelConfig(level_number=15, label="O", x1=1233, y1=678, delay1=1.0),
    LevelConfig(level_number=16, label="P", x1=1150, y1=799, delay1=1.0),
    LevelConfig(level_number=17, label="Q", x1=1354, y1=1133, x2=947, y2=1094, delay2=0.5),
    LevelConfig(level_number=18, label="R", x1=1482, y1=758, delay1=8.0),
    LevelConfig(level_number=19, label="S", x1=1090, y1=796, x2=1583, y2=1138),
    LevelConfig(level_number=20, label="T", x1=1194, y1=1135, delay1=2.0),
    LevelConfig(
        level_number=21,
        label="U",
        x1=1160,
        y1=835,
        x2=1361,
        y2=584,
        delay1=0.0,
        delay2=0.25,
    ),
    LevelConfig(level_number=22, label="V", x1=1297, y1=841),
    LevelConfig(level_number=23, label="W", x1=1325, y1=761),
    LevelConfig(level_number=24, label="X", x1=1276, y1=461, delay1=0.5),
    LevelConfig(
        level_number=25,
        label="Y",
        x1=416,
        y1=581,
        x2=1117,
        y2=801,
        x3=826,
        y3=789,
        delay2=0.5,
        delay3=0.35,
    ),
    LevelConfig(level_number=26, label="Z", x1=1000, y1=833, delay1=0.85),
    # Numbers 0 through 9 (Levels 27 to 36)
    LevelConfig(
        level_number=27,
        label="0",
        x1=489,
        y1=874,
        x2=902,
        y2=1034,
        delay1=0.0,
        delay2=0.5,
    ),
    LevelConfig(
        level_number=28,
        label="1",
        x1=1406,
        y1=747,
        x2=1573,
        y2=888,
        x3=1375,
        y3=1087,
        delay2=1.85,
        delay3=0.25,
    ),
    LevelConfig(level_number=29, label="2", x1=910, y1=1091, reset_time=10.0),
    LevelConfig(level_number=30, label="3", x1=1069, y1=1091, delay1=1.5),
    LevelConfig(level_number=31, label="4", x1=777, y1=608, delay1=0.17),
    LevelConfig(level_number=32, label="5", x1=924, y1=1052),
    LevelConfig(
        level_number=33,
        label="6",
        x1=489,
        y1=876,
        x2=914,
        y2=1030,
        delay1=0.0,
        delay2=0.8,
    ),
    LevelConfig(
        level_number=34,
        label="7",
        x1=122,
        y1=640,
        x2=530,
        y2=792,
        delay1=0.0,
        delay2=0.85,
    ),
    LevelConfig(
        level_number=35,
        label="8",
        x1=122,
        y1=640,
        x2=530,
        y2=792,
        delay1=0.0,
        delay2=0.95,
    ),
    LevelConfig(
        level_number=36,
        label="9",
        x1=1258,
        y1=497,
        x2=1618,
        y2=761,
        delay1=0.0,
        delay2=2.5,
    ),
    # Symbols (Levels 37 to 44)
    LevelConfig(level_number=37, label="<", x1=1779, y1=970),
    LevelConfig(level_number=38, label=">", x1=155, y1=531, reset_time=10.0),
    LevelConfig(
        level_number=39,
        label="#",
        x1=155,
        y1=532,
        x2=1851,
        y2=1119,
        delay1=0.0,
        delay2=3.0,
    ),
    LevelConfig(level_number=40, label="!", x1=740, y1=597, delay1=1.25),
    LevelConfig(level_number=41, label="@", x1=1456, y1=331, delay1=0.0, reset_time=10.0),
    LevelConfig(level_number=42, label="$", x1=137, y1=435, delay1=1.5),
    LevelConfig(level_number=43, label="~", x1=137, y1=435, delay1=0.0),
    LevelConfig(
        level_number=44,
        label="*",
        x1=285,
        y1=839,
        x2=656,
        y2=999,
        delay1=0.0,
        delay2=0.55,
        reset_time=10.0,
    ),
)


async def run_levels(start_level: int = 1, end_level: int = 44) -> None:
    """Execute sequential click routines for all specified game levels.

    Iterates through configured levels between `start_level` and `end_level`,
    dispatching each level's click and wait parameters to `level_template_click`.

    Parameters
    ----------
    start_level : int
        First level to execute (1-indexed), by default 1.
    end_level : int
        Last level to execute inclusive, by default 44.

    Returns
    -------
    None
    """
    for config in LEVEL_CONFIGS:
        if start_level <= config.level_number <= end_level:
            await level_template_click(
                level_number=config.level_number,
                x1=config.x1,
                y1=config.y1,
                x2=config.x2,
                y2=config.y2,
                x3=config.x3,
                y3=config.y3,
                delay1=config.delay1,
                delay2=config.delay2,
                delay3=config.delay3,
                reset_time=config.reset_time,
            )
