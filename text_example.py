from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB

async def run2():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    await DRIVE_BASE.straight(100)
    await DRIVE_BASE.curve(100, 45)
    await DRIVE_BASE.straight(-100)
