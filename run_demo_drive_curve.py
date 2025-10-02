from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB


#curve() is currently described in the docs as:
#Drives an arc along a circle of a given radius, by a given angle.
#It doesn't say anything about how negative values affect anything, so my natural inclination is that it should work like this:
#If the radius is positive, it curves to the right (drives along green line), or if negative, it curves to the left (drives along red line).
#If the angle is positive, it drives forward or if negative, it drives backwards.

async def run2():
    await HUB.speaker.beep()
    HUB.light.on(Color.YELLOW)
    #await DRIVE_BASE.straight(100)
    await DRIVE_BASE.curve(100, 45) #forward right turn 45 degree
    await wait(2000)
    await DRIVE_BASE.curve(100, -45)#forward left turn 45 degree
    await wait(2000)
    await DRIVE_BASE.curve(-100, -45) #backward left turn 45 degree
    await wait(2000)
    await DRIVE_BASE.curve(-100, 45) #backward right turn 45 degree
    await wait(2000)
    #await DRIVE_BASE.straight(-100)


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
        run2()
    )

#run_task(main())

if __name__ == "__main__":
    run_task(main())