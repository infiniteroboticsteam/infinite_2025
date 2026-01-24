from pybricks.parameters import Color, Direction
from pybricks.tools import multitask, run_task, wait



from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT
DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
#this function plays the star wars opening music.

async def test():
    '''await DRIVE_BASE.straight(500)
    await DRIVE_BASE.straight(-500)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.turn(-90)'''
    await CENTER_ATTACHMENT.run_angle(150,-150)
    await CENTER_ATTACHMENT.run_angle(300,150)

#this function tests control of center attachment.
async def reset_motor():
    # Just a demo to show off the center attachment
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    CENTER_ATTACHMENT.reset_angle(0)
    """for count in range(2):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, 90) 
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, -90) """
async def straight(m):
    DRIVE_BASE.straight(m)

async def turn(degrees):
    DRIVE_BASE.turn(degrees)
# write code in "async def mission():" or line 28
async def liftup(speed,degrees):
    await CENTER_ATTACHMENT.run_angle(speed,degrees)


async def run2():
    CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE,gears=[12,20])
    
    DRIVE_BASE.use_gyro(True)
    
    #await liftup(200,135)
    await DRIVE_BASE.straight(325)
        
    await DRIVE_BASE.turn(53)
    await DRIVE_BASE.straight(220)
    #await DRIVE_BASE.turn(-30)
    #await DRIVE_BASE.turn(15)
    #await DRIVE_BASE.straight(150)
    
    await liftup(300,250)
    #await liftup(300,-50)
    DRIVE_BASE.settings(straight_speed=200, straight_acceleration=200)
    await DRIVE_BASE.straight(-400)
    await liftup(200,-25)
    #await DRIVE_BASE.straight(-200)
    #await multitask(FRONT_ATTACHMENT.run_angle(799,160), CENTER_ATTACHMENT.run_angle(100, 110))

    #await liftup(100,-10)
    DRIVE_BASE.settings(straight_speed=300, straight_acceleration=300)
    await DRIVE_BASE.straight(20)
    await liftup(300,-75)
    

    #await wait(500)
    await DRIVE_BASE.turn(-40)
    await DRIVE_BASE.straight(-90)
    await liftup(25,15)
    await DRIVE_BASE.turn(47) #used to be 90
    await liftup(50,44)
    await wait(50)
    await liftup(75,-7.5)
    #await liftup(25,12)
    await DRIVE_BASE.straight(30)
    await DRIVE_BASE.turn(-47) #used to be -90
    DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
    await DRIVE_BASE.straight(-600)
    await liftup(300,-160)
    #await DRIVE_BASE.stop()
    DRIVE_BASE.use_gyro(False) 


if __name__ == "__main__":
    run_task(run2())
