import mouse  # Library to handle mouse events
import time   # Library for sleep functionality


def display_mouse_position():
    """
    Prints the current mouse position to the console.
    Triggered each time the mouse is clicked.
    """
    position = mouse.get_position()  # Get the current mouse position as a tuple (x, y)
    print(f"\nMouse: {position}")    # Print the position in a readable format


# Set up an event listener to trigger on mouse click
mouse.on_click(lambda: display_mouse_position())

print("Listening for mouse clicks. Click anywhere to display the mouse position.")
print("Press Ctrl+C to exit.")  # Inform the user how to exit the script

# Keep the script running to listen for mouse clicks
try:
    while True:
        time.sleep(0.1)  # Sleep briefly to reduce CPU usage
except KeyboardInterrupt:
    print("\nProgram exited.")  # Handle graceful exit on Ctrl+C
