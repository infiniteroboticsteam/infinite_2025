from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from icon_library import INFINITE, display_pulse_icon
from music_library import star_wars_opening
from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

#this function plays the star wars opening music.
async def subtask_play_star_wars():
    await display_pulse_icon(INFINITE) #REBEL)
    # play some music to show off multitasking
    await star_wars_opening()

#this function tests control of center attachment.
async def subtask_test_center_attachment():
    # Just a demo to show off the center attachment
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    CENTER_ATTACHMENT.reset_angle(0)
    for count in range(2):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, 360) #speed, angle
        await wait(500)
        await CENTER_ATTACHMENT.run_time(300, -360) 
 

#use this function as a template to define how to drive the base
async def subtask_test_drive_base():
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

async def run1():
    await wait(0)
    # Just a demo to show off the drivebase as well as music, icons,
    # and multitasking
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    await HUB.speaker.beep(500, 400)
    await multitask(
        subtask_play_star_wars(),
        subtask_test_drive_base(),
        #subtask_test_center_attachment()
        )

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
        run1()
    )

#run_task(main())

if __name__ == "__main__":
    run_task(main())