import asyncio
import keyboard
from Levels import run_levels  # Import function to run game levels
# Import function for mouse click actions
from common import mouse_click


# Simulates a mouse click at a specific screen coordinate
async def press_start():
    """
    Simulates a mouse click at the coordinates (408, 1255).
    Used to start the game.
    """
    await mouse_click(408, 1255)


# Main game logic: Starts the game and runs through all levels
async def run_game():
    """
    Initiates the game by clicking 'start' and runs through the game levels.
    """
    await press_start()
    await run_levels()

# Main program loop to handle keyboard inputs and control the game


async def main():
    """
    Entry point for the program. 
    - Waits for the 'Enter' key to start the game.
    - Allows the user to exit the program by pressing 'Esc'.
    """
    print("Press Enter to start the game. Press Esc to stop the program.")

    game_task = None  # Keeps track of the current game task

    while True:
        # Start the game if 'Enter' is pressed and no game is running
        if keyboard.is_pressed('enter') and game_task is None:
            print("Game started!")
            game_task = asyncio.create_task(
                run_game())  # Start the game task in the background

        # Exit the program if 'Esc' is pressed
        elif keyboard.is_pressed('esc'):
            print("Program exited.")
            if game_task and not game_task.done():
                game_task.cancel()  # Cancel the game task if still running
            break

        # Sleep briefly to prevent high CPU usage
        await asyncio.sleep(0.1)


# Run the main function
if __name__ == "__main__":
    """
    Ensures the script runs the `main()` function when executed directly.
    """
    asyncio.run(main())
