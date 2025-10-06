from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

#use this function as a template to define how to drive the base
async def RH_Mission():
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True) 
    #await DRIVE_BASE.straight(100) #in mm
    for count in range(1):
        await wait(1000) #wait for 1000 ms
        await DRIVE_BASE.straight(50) #go straight forward 50 mm
        await DRIVE_BASE.turn(180) #turn right 180 degree
        await wait(1000) 
        await DRIVE_BASE.straight(-50) #go straight backward 50 mm
        await DRIVE_BASE.turn(-180)#, then=Stop.COAST ) #turn left 180 degree
    #await DRIVE_BASE.straight(-10)
    DRIVE_BASE.use_gyro(False)

#used to combine tasks
async def run1():
    await wait(0)
    # Just a demo to show off the drivebase as well as music, icons,
    # and multitasking
    # Turn button yellow; and beep/wait so hands are out of the way
    await RH_Mission()

#################################################
# Do not remove the code below.
# this code is used for testing run1() as in this example.
# if you changed the function name run1, change it in the function main1 as well.
##################################################
#boilerplate to run missions solved in this code
async def main():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
        RH_Mission()
    )

#run_task(main())

if __name__ == "__main__":
    run_task(main())