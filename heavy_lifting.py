from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase



from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT

#use this function as a template to define how to drive the base
async def drive_base_to_heavy_lifting():
    await set_drivebase()

    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True) 
    await wait(1000) #wait for 1000 ms
    await DRIVE_BASE.straight(735)
    await DRIVE_BASE.turn(44)
    await DRIVE_BASE.straight(105)
    await CENTER_ATTACHMENT.run_angle(80, -250)
    await wait(1000)
    await CENTER_ATTACHMENT.run_angle(80,250)  
    await DRIVE_BASE.straight(-10)
    #reverse steps to go back
    await DRIVE_BASE.turn(-80)
    await DRIVE_BASE.straight(45)

    DRIVE_BASE.settings(turn_rate=100,turn_acceleration=50)
    await DRIVE_BASE.arc(radius=-20, angle=150) #forward left turn 45 degree
    await DRIVE_BASE.straight(40)
    await DRIVE_BASE.turn(100)
    await DRIVE_BASE.straight(-500)
    await wait(2000)
    await DRIVE_BASE.straight(500)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(735)
    return
    await DRIVE_BASE.straight(740)
    #await DRIVE_BASE.straight(20)
   
if __name__ == "__main__":
    run_task(drive_base_to_heavy_lifting())