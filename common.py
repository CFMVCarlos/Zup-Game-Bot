import asyncio
import time
import mouse
import pyautogui
from PIL import ImageGrab

# Screen dimensions for coordinate scaling
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()


def convert_coords(x, y):
    """
    Convert coordinates from a 2560x1440 resolution to the current screen resolution.
    """
    return x * SCREEN_WIDTH / 2560, y * SCREEN_HEIGHT / 1440


async def mouse_click(x, y):
    """
    Simulate a mouse click at the specified coordinates after scaling them to the screen resolution.
    """
    await asyncio.sleep(0.1)  # Brief delay before the click
    mouse.move(*convert_coords(x, y), absolute=True)
    mouse.click('left')
    await asyncio.sleep(0.1)  # Brief delay after the click


# Pre-compute coordinates and bounding box for checkOut optimization
_checkout_original_coords = [
    (2357, 1070),
    (2357, 1162),
    (2357, 1283)
]
_scaled_coords = [(int(x), int(y)) for x, y in [convert_coords(cx, cy) for cx, cy in _checkout_original_coords]]
_min_x = min(x for x, y in _scaled_coords)
_max_x = max(x for x, y in _scaled_coords)
_min_y = min(y for x, y in _scaled_coords)
_max_y = max(y for x, y in _scaled_coords)
_checkout_bbox = (_min_x, _min_y, _max_x + 1, _max_y + 1)
_checkout_local_coords = [(x - _min_x, y - _min_y) for x, y in _scaled_coords]


def checkOut():
    """
    Check the RGB values of three specific screen locations to determine if a certain condition is met.
    Returns True if any of the points exceed the RGB threshold.
    """
    # Grab only the bounding box containing our target pixels for massive performance gain
    screen = ImageGrab.grab(bbox=_checkout_bbox).load()

    # 190 + 255 + 255
    threshold = 700

    # Check if any of the points exceed the threshold
    for x, y in _checkout_local_coords:
        # Check only first 3 channels (RGB) to safely support RGBA captures if present
        if sum(screen[x, y][:3]) > threshold:
            return True
    return False


async def Out():
    """
    Simulate a mouse click to mark the completion of a level.
    """
    await mouse_click(2357, 1161)


async def Reset():
    """
    Simulate a mouse click to reset the level.
    """
    await mouse_click(73, 1376)
    await asyncio.sleep(0.5)


async def level_template_click(level_number, x1, y1, x2=None, y2=None, x3=None, y3=None, delay1=None, delay2=None, delay3=None, reset_time=5):
    """
    Handles the actions required to complete a level, including retries on timeout.

    Parameters:
    - level_number: The level number for logging purposes.
    - x1, y1: Required primary coordinates to click.
    - x2, y2: Optional second set of coordinates to click.
    - x3, y3: Optional third set of coordinates to click.
    - delay1, delay2, delay3: Optional delays between actions.
    """
    while True:  # Retry loop for timeout scenarios
        await Reset()  # Reset the level

        if delay1:
            await asyncio.sleep(delay1)

        await mouse_click(x1, y1)  # Click the primary location

        if delay2:
            await asyncio.sleep(delay2)

        if x2 and y2:  # Click the secondary location if provided
            await mouse_click(x2, y2)

        if delay3:
            await asyncio.sleep(delay3)

        if x3 and y3:  # Click the tertiary location if provided
            await mouse_click(x3, y3)

        # Start timeout countdown
        start_time = time.time()
        while checkOut():  # Check for completion condition
            if time.time() - start_time > reset_time:  # Timeout after some seconds
                print(f"Timeout occurred. Restarting Level {level_number}...")
                break  # Retry the level
            await asyncio.sleep(0.01)  # Avoid busy waiting
        else:
            # If checkOut() condition is no longer True, mark the level as complete
            await Out()
            print(f"Level {level_number} completed!")
            break  # Exit retry loop


# Entry point for testing the script
if __name__ == "__main__":
    asyncio.run(level_template_click(1, 1303, 800))
