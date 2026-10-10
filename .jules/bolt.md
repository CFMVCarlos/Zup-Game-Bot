## 2024-06-25 - Bounding box optimization for ImageGrab.grab()
**Learning:** Calling `ImageGrab.grab()` continuously in a loop for full-screen resolution (e.g., 2560x1440) creates a massive performance bottleneck, particularly because we only needed to check a few specific coordinates.
**Action:** Always pre-compute the target coordinates to construct a minimal bounding box (`bbox`). Pass this bounding box into `ImageGrab.grab(bbox=...)` to capture only the small subset of the screen, which drastically improves performance. Ensure you calculate relative coordinates within the captured bounding box for pixel checking.
## 2024-05-18 - [Optimizing CheckOut Function with Bounding Box]
**Learning:** The checkOut function captured the full screen on every iteration which was incredibly slow. By limiting ImageGrab to a small bounding box surrounding the expected checkout coordinates, CPU usage is minimized and cycle times are drastically improved.
**Action:** Always constrain screenshot/pixel checks to the smallest necessary bounding box rather than capturing the entire screen.
