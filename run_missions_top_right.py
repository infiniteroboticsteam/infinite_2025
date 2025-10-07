from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT

#use this function as a template to define how to drive the base
async def drive_base_to_heavy_lifting():
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True) 
    await DRIVE_BASE.straight(740)
    await DRIVE_BASE.turn(45)
    await DRIVE_BASE.straight(70)
    #reverse steps to go back
    await DRIVE_BASE.straight(-70)
    await DRIVE_BASE.turn(-45)
    await DRIVE_BASE.straight(-740)
    DRIVE_BASE.use_gyro(False)

if __name__ == "__main__":
    run_task(drive_base_to_heavy_lifting())