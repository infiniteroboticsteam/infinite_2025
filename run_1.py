from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from icon_library import REBEL, display_pulse_icon
from music_library import star_wars_opening
from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def subtask_play_start_wars():
    await display_pulse_icon(REBEL)
    # play some music to show off multitasking
    await star_wars_opening()


async def subtask_test_center_attachment():
    # Just a demo to show off the center attachment
    CENTER_ATTACHMENT.reset_angle(0)
    for count in range(2):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(300, 360) 
        await wait(500)
        await CENTER_ATTACHMENT.run_time(300, -360) 
    
async def subtask_test_drive_base():
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True)
    #await DRIVE_BASE.straight(100) #in mm
    for count in range(1):
        await wait(1000)
        await DRIVE_BASE.straight(50)
        await DRIVE_BASE.turn(180)
        await wait(1000)
        await DRIVE_BASE.straight(-50)
        await DRIVE_BASE.turn(-180)
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
        #subtask_play_start_wars(),
        subtask_test_drive_base(),
        subtask_test_center_attachment()
    )


#boilerplate to run missions solved in this code
async def main():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
        run1()
    )

if __name__ == "__main__":
    run_task(main())