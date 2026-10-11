"""Common utilities for screen coordinate conversion, mouse input, and pixel detection.

This module provides reusable asynchronous functions for scaling mouse coordinates
from a reference 2560x1440 resolution to arbitrary monitor resolutions, triggering
left-clicks, resetting level states, and sampling target screen pixels to verify level
completion in Zup!.
"""

from __future__ import annotations

import asyncio
import time
from typing import Final

import mouse
import pyautogui
from PIL import ImageGrab

# Reference screen dimensions for coordinate normalization
REFERENCE_WIDTH: Final[int] = 2560
REFERENCE_HEIGHT: Final[int] = 1440

# Screen dimensions for coordinate scaling with safe fallback
try:
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
except Exception:
    SCREEN_WIDTH, SCREEN_HEIGHT = REFERENCE_WIDTH, REFERENCE_HEIGHT


def convert_coords(x: float | int, y: float | int) -> tuple[int, int]:
    """Convert coordinates from 2560x1440 resolution to active display resolution.

    Scales horizontal and vertical pixel positions proportionally according
    to the active display resolution relative to the base 2560x1440 reference.

    Parameters
    ----------
    x : float | int
        X-coordinate in reference 2560x1440 resolution.
    y : float | int
        Y-coordinate in reference 2560x1440 resolution.

    Returns
    -------
    tuple[int, int]
        Scaled (x, y) coordinates rounded to integers for display positioning.
    """
    scaled_x = int(round(x * SCREEN_WIDTH / REFERENCE_WIDTH))
    scaled_y = int(round(y * SCREEN_HEIGHT / REFERENCE_HEIGHT))
    return scaled_x, scaled_y


async def mouse_click(x: int, y: int, delay: float = 0.1) -> None:
    """Simulate a mouse click at specified coordinates after scaling.

    Moves the cursor to scaled screen coordinates and performs a left-click
    with brief async pauses before and after the action.

    Parameters
    ----------
    x : int
        Target horizontal coordinate in reference resolution.
    y : int
        Target vertical coordinate in reference resolution.
    delay : float
        Delay in seconds before and after the click, by default 0.1.

    Returns
    -------
    None
    """
    await asyncio.sleep(delay)
    scaled_x, scaled_y = convert_coords(x, y)
    mouse.move(scaled_x, scaled_y, absolute=True)
    mouse.click("left")
    await asyncio.sleep(delay)


# Pre-compute coordinates and bounding box for checkOut optimization
_CHECKOUT_ORIGINAL_COORDS: Final[tuple[tuple[int, int], ...]] = (
    (2357, 1070),
    (2357, 1162),
    (2357, 1283),
)

_scaled_coords: list[tuple[int, int]] = [
    convert_coords(cx, cy) for cx, cy in _CHECKOUT_ORIGINAL_COORDS
]
_min_x: int = min(pt[0] for pt in _scaled_coords)
_max_x: int = max(pt[0] for pt in _scaled_coords)
_min_y: int = min(pt[1] for pt in _scaled_coords)
_max_y: int = max(pt[1] for pt in _scaled_coords)

_CHECKOUT_BBOX: Final[tuple[int, int, int, int]] = (
    _min_x,
    _min_y,
    _max_x + 1,
    _max_y + 1,
)
_CHECKOUT_LOCAL_COORDS: Final[tuple[tuple[int, int], ...]] = tuple(
    (pt[0] - _min_x, pt[1] - _min_y) for pt in _scaled_coords
)


def checkOut(threshold: int = 700) -> bool:
    """Check RGB values of target screen pixels to determine level completion state.

    Captures the pre-computed bounding box encompassing verification points and
    evaluates whether any sampled point exceeds the RGB brightness threshold.

    Parameters
    ----------
    threshold : int
        Combined RGB brightness threshold, by default 700.

    Returns
    -------
    bool
        True if any of the target points exceed the threshold, False otherwise.
    """
    try:
        screen = ImageGrab.grab(bbox=_CHECKOUT_BBOX).load()
        if screen is None:
            return False

        for lx, ly in _CHECKOUT_LOCAL_COORDS:
            pixel = screen[lx, ly]
            if isinstance(pixel, (tuple, list)):
                brightness = float(sum(pixel[:3]))
            elif isinstance(pixel, (int, float)):
                brightness = float(pixel)
            else:
                brightness = 0.0

            if brightness > threshold:
                return True
    except Exception:
        return False
    return False


async def Out() -> None:
    """Simulate a mouse click to complete and exit the current level.

    Clicks the completion / next level button located at reference
    coordinates (2357, 1161).

    Returns
    -------
    None
    """
    await mouse_click(2357, 1161)


async def Reset() -> None:
    """Simulate a mouse click to reset the current level.

    Clicks the reset button located at reference coordinates (73, 1376)
    followed by a short pause to allow the game state to reinitialize.

    Returns
    -------
    None
    """
    await mouse_click(73, 1376)
    await asyncio.sleep(0.5)


async def level_template_click(
    level_number: int,
    x1: int,
    y1: int,
    x2: int | None = None,
    y2: int | None = None,
    x3: int | None = None,
    y3: int | None = None,
    delay1: float | None = None,
    delay2: float | None = None,
    delay3: float | None = None,
    reset_time: float = 5.0,
) -> None:
    """Execute the click sequence and verification polling for an individual level.

    Performs an initial reset, executes up to three sequential clicks with
    customizable timing delays, and polls the completion condition until resolved
    or timed out. If a timeout occurs, the level sequence restarts automatically.

    Parameters
    ----------
    level_number : int
        The level identifier for logging and tracking.
    x1 : int
        Primary target horizontal coordinate in reference resolution.
    y1 : int
        Primary target vertical coordinate in reference resolution.
    x2 : int | None
        Secondary target horizontal coordinate, by default None.
    y2 : int | None
        Secondary target vertical coordinate, by default None.
    x3 : int | None
        Tertiary target horizontal coordinate, by default None.
    y3 : int | None
        Tertiary target vertical coordinate, by default None.
    delay1 : float | None
        Delay in seconds prior to first click, by default None.
    delay2 : float | None
        Delay in seconds prior to second click, by default None.
    delay3 : float | None
        Delay in seconds prior to third click, by default None.
    reset_time : float
        Maximum seconds to wait for level completion before retrying, by default 5.0.

    Returns
    -------
    None
    """
    while True:
        await Reset()

        if delay1 is not None and delay1 > 0:
            await asyncio.sleep(delay1)

        await mouse_click(x1, y1)

        if delay2 is not None and delay2 > 0:
            await asyncio.sleep(delay2)

        if x2 is not None and y2 is not None:
            await mouse_click(x2, y2)

        if delay3 is not None and delay3 > 0:
            await asyncio.sleep(delay3)

        if x3 is not None and y3 is not None:
            await mouse_click(x3, y3)

        # Polling loop for completion state
        start_time = time.time()
        while checkOut():
            if time.time() - start_time > reset_time:
                print(f"Timeout occurred. Restarting Level {level_number}...")
                break
            await asyncio.sleep(0.01)
        else:
            await Out()
            print(f"Level {level_number} completed!")
            break


if __name__ == "__main__":
    asyncio.run(level_template_click(1, 1303, 800))
