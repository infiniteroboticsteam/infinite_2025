from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT

async def drive_base_to_heavy_lifting():
    await CENTER_ATTACHMENT.run_angle(300, -200) #lower the attachment
    return
    DRIVE_BASE.use_gyro(True)
    #await (1000) #wait for 1000 ms
    await DRIVE_BASE.straight(740) #go straight forward 740 mm
    await DRIVE_BASE.turn(45) #turn right 45 degree
    await DRIVE_BASE.straight(90)
    #await(4000)
    await DRIVE_BASE.straight(-75)
    await DRIVE_BASE.turn(-45) #turn left 45 degree
    await DRIVE_BASE.straight(-740) #go straight backward 740 mm    
    DRIVE_BASE.use_gyro(False)

if __name__ == "__main__":
    run_task(drive_base_to_heavy_lifting())                                                 