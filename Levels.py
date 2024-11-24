import asyncio
# Import the level interaction function
from common import level_template_click


# Function to execute a sequence of level clicks
async def run_levels():
    """
    Runs through a predefined sequence of levels by simulating clicks at specific coordinates.
    Each level may have different coordinates, delays, or additional parameters.
    """
    # A
    await level_template_click(1, 1303, 800)
    # B
    await level_template_click(2, 1245, 800)
    # C
    await level_template_click(3, 1245, 800)
    # D
    await level_template_click(4, 1245, 800)
    # E
    await level_template_click(5, 1234, 760)
    # F
    await level_template_click(6, 1410, 803)
    # G
    await level_template_click(7, 1232, 808)
    # H
    await level_template_click(8, 1159, 802)
    # I
    await level_template_click(9, 1276, 556, delay1=0.5)
    # J
    await level_template_click(10, 1186, 591)
    # K
    await level_template_click(11, 1232, 764)
    # L
    await level_template_click(12, 1359, 716, delay1=0.65)
    # M
    await level_template_click(13, 1361, 636, delay1=0.5)
    # N
    await level_template_click(14, 1269, 678)
    # O
    await level_template_click(15, 1233, 678, delay1=1)
    # P
    await level_template_click(16, 1150, 799, delay1=1)
    # Q
    await level_template_click(17, 1354, 1133, 947, 1094, delay2=0.5)
    # R
    await level_template_click(18, 1482, 758, delay1=8)
    # S
    await level_template_click(19, 1090, 796, 1583, 1138)
    # T
    await level_template_click(20, 1194, 1135, delay1=2)
    # U
    await level_template_click(21, 1160, 835, 1361, 584, delay1=0, delay2=0.25)
    # V
    await level_template_click(22, 1297, 841)
    # W
    await level_template_click(23, 1325, 761)
    # X
    await level_template_click(24, 1276, 461, delay1=0.5)
    # Y
    await level_template_click(25, 416, 581, 1117, 801, 826, 789, delay2=0.5, delay3=0.35)
    # Z
    await level_template_click(26, 1000, 833, delay1=0.85)
    # 0
    await level_template_click(27, 489, 874, 902, 1034, delay1=0, delay2=0.5)
    # 1
    await level_template_click(28, 1406, 747, 1573, 888, 1375, 1087, delay2=1.85, delay3=0.25)
    # 2
    await level_template_click(29, 910, 1091, reset_time=10)
    # 3
    await level_template_click(30, 1069, 1091, delay1=1.5)
    # 4
    await level_template_click(31, 777, 608, delay1=0.17)
    # 5
    await level_template_click(32, 924, 1052)
    # 6
    await level_template_click(33, 489, 876, 914, 1030, delay1=0, delay2=0.8)
    # 7
    await level_template_click(34, 122, 640, 530, 792, delay1=0, delay2=0.85)
    # 8
    await level_template_click(35, 122, 640, 530, 792, delay1=0, delay2=0.95)
    # 9
    await level_template_click(36, 1258, 497, 1618, 761, delay1=0, delay2=2.5)
    # <
    await level_template_click(37, 1779, 970)
    # >
    await level_template_click(38, 155, 531, reset_time=10)
    # #
    await level_template_click(39, 155, 532, 1851, 1119, delay1=0, delay2=3)
    # !
    await level_template_click(40, 740, 597, delay1=1.25)
    # @
    await level_template_click(41, 1456, 331, delay1=0, reset_time=10)
    # $
    await level_template_click(42, 137, 435, delay1=1.5)
    # ~
    await level_template_click(43, 137, 435, delay1=0)
    # *
    await level_template_click(44, 285, 839, 656, 999, delay1=0, delay2=0.55, reset_time=10)
