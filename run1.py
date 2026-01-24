from pybricks.parameters import Color, Direction
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT,FRONT_ATTACHMENT

DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)

#use this function as a template to define how to drive the base
#drive_base_to_heavy_lifting
async def run1():
    DRIVE_BASE.use_gyro(True) 
    await set_drivebase()
    CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,
                                  gears=[12,36])
    # Turn on Gyro, drive forward
    await wait(100)
    await DRIVE_BASE.straight(625)
    #return
    await DRIVE_BASE.turn(42)
    #return
    #slow down for more precision
    #approach for heavy lifting 
    await DRIVE_BASE.straight(111)
    #return

    await wait(100)
    
    #return
  
    await wait(255)
    await multitask(FRONT_ATTACHMENT.run_angle(799,160), CENTER_ATTACHMENT.run_angle(100, 110))
    #return
    await CENTER_ATTACHMENT.run_angle(70,-120)
    #return 
    
    await DRIVE_BASE.straight(-120)
    await FRONT_ATTACHMENT.run_angle(500,100)
    
    await DRIVE_BASE.turn(-40)
    await DRIVE_BASE.straight(140)
    await DRIVE_BASE.turn(-10)
    await FRONT_ATTACHMENT.run_angle(200,-90)
    await DRIVE_BASE.straight(-799)
    
    DRIVE_BASE.use_gyro(False) 

    

if __name__ == "__main__":
    run_task(run1())