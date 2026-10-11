"""Utility tool to inspect real-time mouse cursor screen coordinates.

Listens for user mouse clicks and outputs the current cursor position to stdout.
Useful for identifying click targets and calibrating game level coordinates.
"""

from __future__ import annotations

import time

import mouse


def get_mouse_position() -> tuple[int, int]:
    """Retrieve current screen coordinates of mouse cursor.

    Queries the operating system mouse driver for active X and Y positions.

    Returns
    -------
    tuple[int, int]
        Active cursor screen coordinates formatted as (x, y).
    """
    pos = mouse.get_position()
    return int(pos[0]), int(pos[1])


def display_mouse_position() -> None:
    """Print current mouse cursor coordinates to the terminal console.

    Invoked as an event callback upon registering a mouse click event.

    Returns
    -------
    None
    """
    position = get_mouse_position()
    print(f"\nMouse: {position}")


def main() -> None:
    """Initialize mouse click listener and run polling loop until interrupted.

    Registers a global click hook to log cursor coordinates and cleanly unhooks
    listeners upon catching a KeyboardInterrupt or termination signal.

    Returns
    -------
    None
    """
    # Set up an event listener to trigger on mouse click
    mouse.on_click(display_mouse_position)

    print("Listening for mouse clicks. Click anywhere to display the mouse position.")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nProgram exited.")
    finally:
        mouse.unhook_all()


if __name__ == "__main__":
    main()
