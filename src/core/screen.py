import asyncio
import time
import mouse
import pyautogui
from PIL import ImageGrab

class ScreenCore:
    """
    Core utilities for interacting with screen coordinates and checking screen pixels.
    """
    def __init__(self, original_resolution=(2560, 1440)):
        self.original_width, self.original_height = original_resolution
        self.screen_width, self.screen_height = pyautogui.size()
        
        # Pre-compute checkout coordinates for optimal performance
        self._checkout_original_coords = [
            (2357, 1070),
            (2357, 1162),
            (2357, 1283)
        ]
        
        self._scaled_coords = [(int(x), int(y)) for x, y in [self.convert_coords(cx, cy) for cx, cy in self._checkout_original_coords]]
        
        # Ensure we have a valid bounding box even if scaled coords are empty or malformed
        if self._scaled_coords:
            self._min_x = min(x for x, y in self._scaled_coords)
            self._max_x = max(x for x, y in self._scaled_coords)
            self._min_y = min(y for x, y in self._scaled_coords)
            self._max_y = max(y for x, y in self._scaled_coords)
            self._checkout_bbox = (self._min_x, self._min_y, self._max_x + 1, self._max_y + 1)
            self._checkout_local_coords = [(x - self._min_x, y - self._min_y) for x, y in self._scaled_coords]
        else:
            self._checkout_bbox = (0, 0, 1, 1)
            self._checkout_local_coords = []

    def convert_coords(self, x: float, y: float) -> tuple[float, float]:
        """
        Converts coordinates from the original resolution to the current screen resolution.
        """
        return x * self.screen_width / self.original_width, y * self.screen_height / self.original_height

    async def mouse_click(self, x: float, y: float):
        """
        Simulates a scaled mouse click at the given coordinates.
        """
        await asyncio.sleep(0.1)
        try:
            # Attempt to use 'mouse' (which works well on Windows, but often fails on Linux without root)
            coords = self.convert_coords(x, y)
            mouse.move(coords[0], coords[1], absolute=True)
            mouse.click('left')
        except ImportError:
            # Fallback to pyautogui which does not need root on Linux for clicking
            coords = self.convert_coords(x, y)
            pyautogui.click(coords[0], coords[1])
        await asyncio.sleep(0.1)

    def check_out(self) -> bool:
        """
        Checks the RGB values of specific screen locations to determine if a condition is met.
        Highly optimized by only capturing the minimal necessary bounding box.
        """
        if not self._checkout_bbox:
            return False
            
        screen = ImageGrab.grab(bbox=self._checkout_bbox).load()
        threshold = 700

        for x, y in self._checkout_local_coords:
            try:
                # Check RGB values (first 3 channels)
                if sum(screen[x, y][:3]) > threshold:
                    return True
            except IndexError:
                pass
        return False
