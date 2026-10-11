"""Main execution orchestrator for Zup! automated gameplay bot.

Listens for keyboard input to start the automated sequence or exit gracefully.
Initiates game startup and runs through configured level automation routines.
"""

from __future__ import annotations

import asyncio
from typing import Final

import keyboard

from src.common import mouse_click
from src.Levels import run_levels

START_BUTTON_COORDS: Final[tuple[int, int]] = (408, 1255)


async def press_start() -> None:
    """Simulate a mouse click at the start menu coordinates.

    Dispatches a left click to the game start button at reference coordinates
    (408, 1255).

    Returns
    -------
    None
    """
    await mouse_click(*START_BUTTON_COORDS)


async def run_game() -> None:
    """Initiate game startup and execute all level sequences sequentially.

    Clicks the game start button and invokes the level automation loop
    until all levels are completed.

    Returns
    -------
    None
    """
    await press_start()
    await run_levels()


async def main() -> None:
    """Handle keyboard input loop and lifecycle of the automation task.

    Polls keyboard state for control hotkeys:
    - Press 'Enter' to start level automation if not already running.
    - Press 'Esc' to cancel active execution and exit the program.

    Returns
    -------
    None
    """
    print("Press Enter to start the game. Press Esc to stop the program.")

    game_task: asyncio.Task[None] | None = None

    while True:
        if keyboard.is_pressed("enter") and game_task is None:
            print("Game started!")
            game_task = asyncio.create_task(run_game())

        elif keyboard.is_pressed("esc"):
            print("Program exited.")
            if game_task is not None and not game_task.done():
                game_task.cancel()
                try:
                    await game_task
                except asyncio.CancelledError:
                    pass
            break

        await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())
