from pybricks.tools import run_task, wait
from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT
from library import set_drivebase
from pybricks.tools import run_task, wait
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor




#use this function as a template to define how to drive the base
async def run4():

    await set_drivebase()
    #CENTER_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)
    #CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,gears=[12,20])
    
    # Turn on Gyro
    DRIVE_BASE.use_gyro(True)

    #await CENTER_ATTACHMENT.run_angle(100,120)
    DRIVE_BASE.settings(straight_speed=700,straight_acceleration=650)
    await DRIVE_BASE.straight(-600)
    #await DRIVE_BASE.straight(-350) #to be deleted at coach's house
    await DRIVE_BASE.straight(140)
    DRIVE_BASE.settings(straight_speed=360,straight_acceleration=360)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(30)
    await CENTER_ATTACHMENT.run_angle(100,-120)
    DRIVE_BASE.settings(straight_speed=600,straight_acceleration=650)
    await DRIVE_BASE.straight(-82)
    await CENTER_ATTACHMENT.run_angle(100,90)
    await DRIVE_BASE.straight(250) # move back
    DRIVE_BASE.settings(straight_speed=280,straight_acceleration=280)
    await DRIVE_BASE.turn(-135) #End of Mission 1
    await DRIVE_BASE.straight(260)
    #await DRIVE_BASE.straight(200) #To be deleted at coach's house
    await CENTER_ATTACHMENT.run_angle(100,-100)
    #await DRIVE_BASE.straight(-120)
    DRIVE_BASE.settings(straight_speed=360,straight_acceleration=440)
    await DRIVE_BASE.straight(-270)
    await DRIVE_BASE.turn(-100)
    await DRIVE_BASE.straight(530)
    
    #await DRIVE_BASE.stop()
    DRIVE_BASE.use_gyro(False) 




if __name__ == "__main__":
    run_task(run4())