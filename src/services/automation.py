import asyncio
import time
import logging
from typing import Optional, List, Dict
from src.core.screen import ScreenCore

logger = logging.getLogger(__name__)

class AutomationService:
    """
    Service responsible for executing the game levels and handling state.
    """
    def __init__(self):
        self.screen_core = ScreenCore()
        self.is_running = False
        self._task: Optional[asyncio.Task] = None
        
        # Predefined levels mapped from the original ZUP.py/Levels.py
        self.levels_sequence = [
            (1, (1303, 800), {}),
            (2, (1245, 800), {}),
            (3, (1245, 800), {}),
            (4, (1245, 800), {}),
            (5, (1234, 760), {}),
            (6, (1410, 803), {}),
            (7, (1232, 808), {}),
            (8, (1159, 802), {}),
            (9, (1276, 556), {"delay1": 0.5}),
            (10, (1186, 591), {}),
            (11, (1232, 764), {}),
            (12, (1359, 716), {"delay1": 0.65}),
            (13, (1361, 636), {"delay1": 0.5}),
            (14, (1269, 678), {}),
            (15, (1233, 678), {"delay1": 1}),
            (16, (1150, 799), {"delay1": 1}),
            (17, (1354, 1133), {"x2": 947, "y2": 1094, "delay2": 0.5}),
            (18, (1482, 758), {"delay1": 8}),
            (19, (1090, 796), {"x2": 1583, "y2": 1138}),
            (20, (1194, 1135), {"delay1": 2}),
            (21, (1160, 835), {"x2": 1361, "y2": 584, "delay1": 0, "delay2": 0.25}),
            (22, (1297, 841), {}),
            (23, (1325, 761), {}),
            (24, (1276, 461), {"delay1": 0.5}),
            (25, (416, 581), {"x2": 1117, "y2": 801, "x3": 826, "y3": 789, "delay2": 0.5, "delay3": 0.35}),
            (26, (1000, 833), {"delay1": 0.85}),
            (27, (489, 874), {"x2": 902, "y2": 1034, "delay1": 0, "delay2": 0.5}),
            (28, (1406, 747), {"x2": 1573, "y2": 888, "x3": 1375, "y3": 1087, "delay2": 1.85, "delay3": 0.25}),
            (29, (910, 1091), {"reset_time": 10}),
            (30, (1069, 1091), {"delay1": 1.5}),
            (31, (777, 608), {"delay1": 0.17}),
            (32, (924, 1052), {}),
            (33, (489, 876), {"x2": 914, "y2": 1030, "delay1": 0, "delay2": 0.8}),
            (34, (122, 640), {"x2": 530, "y2": 792, "delay1": 0, "delay2": 0.85}),
            (35, (122, 640), {"x2": 530, "y2": 792, "delay1": 0, "delay2": 0.95}),
            (36, (1258, 497), {"x2": 1618, "y2": 761, "delay1": 0, "delay2": 2.5}),
            (37, (1779, 970), {}),
            (38, (155, 531), {"reset_time": 10}),
            (39, (155, 532), {"x2": 1851, "y2": 1119, "delay1": 0, "delay2": 3}),
            (40, (740, 597), {"delay1": 1.25}),
            (41, (1456, 331), {"delay1": 0, "reset_time": 10}),
            (42, (137, 435), {"delay1": 1.5}),
            (43, (137, 435), {"delay1": 0}),
            (44, (285, 839), {"x2": 656, "y2": 999, "delay1": 0, "delay2": 0.55, "reset_time": 10}),
        ]

    async def _reset_level(self):
        """Simulate clicking the reset button."""
        await self.screen_core.mouse_click(73, 1376)
        await asyncio.sleep(0.5)

    async def _out(self):
        """Simulate clicking the 'Out' or next level marker."""
        await self.screen_core.mouse_click(2357, 1161)

    async def _press_start(self):
        """Simulate clicking 'start'."""
        await self.screen_core.mouse_click(408, 1255)

    async def _run_level_template(self, level_number: int, x1: float, y1: float, **kwargs):
        """
        Executes a single level template, handling retry logic.
        """
        x2 = kwargs.get('x2')
        y2 = kwargs.get('y2')
        x3 = kwargs.get('x3')
        y3 = kwargs.get('y3')
        delay1 = kwargs.get('delay1')
        delay2 = kwargs.get('delay2')
        delay3 = kwargs.get('delay3')
        reset_time = kwargs.get('reset_time', 5)

        while self.is_running:
            await self._reset_level()

            if delay1: await asyncio.sleep(delay1)
            await self.screen_core.mouse_click(x1, y1)

            if delay2: await asyncio.sleep(delay2)
            if x2 and y2: await self.screen_core.mouse_click(x2, y2)

            if delay3: await asyncio.sleep(delay3)
            if x3 and y3: await self.screen_core.mouse_click(x3, y3)

            start_time = time.time()
            
            level_completed = False
            while self.is_running and self.screen_core.check_out():
                if time.time() - start_time > reset_time:
                    logger.info(f"Timeout on level {level_number}. Retrying...")
                    break
                await asyncio.sleep(0.01)
            else:
                if self.is_running:
                    await self._out()
                    logger.info(f"Level {level_number} completed.")
                    level_completed = True
            
            if level_completed or not self.is_running:
                break

    async def _run_sequence(self):
        """Executes all predefined game levels."""
        try:
            await self._press_start()
            for level_num, (x1, y1), kwargs in self.levels_sequence:
                if not self.is_running:
                    break
                await self._run_level_template(level_num, x1, y1, **kwargs)
        except Exception as e:
            logger.error(f"Error in automation sequence: {e}")
        finally:
            self.is_running = False

    def start(self):
        """Starts the automation service."""
        if not self.is_running:
            self.is_running = True
            self._task = asyncio.create_task(self._run_sequence())

    def stop(self):
        """Stops the automation service."""
        self.is_running = False
        if self._task and not self._task.done():
            self._task.cancel()

    def get_status(self) -> Dict:
        """Returns the current state of the automation."""
        return {
            "status": "running" if self.is_running else "stopped"
        }
