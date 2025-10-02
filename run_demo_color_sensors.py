from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from icon_library import INFINITE, display_pulse_icon
from music_library import star_wars_opening
from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor

from run_demo_drive import subtask_play_star_wars

LEFT_COLOR_SENSOR = ColorSensor(Port.A)
RIGHT_COLOR_SENSOR = ColorSensor(Port.E)

# This is a function that waits for a desired color.
async def wait_for_color(desired_color):
    # While the color is not the desired color, we keep waiting.
    print("waiting for color.")
    while await LEFT_COLOR_SENSOR.color() != desired_color:
        print("color is ", await LEFT_COLOR_SENSOR.color())
        await wait(1000)
    print("color ", desired_color, " is detected!")
    await HUB.speaker.beep(500, 400)
    return True

async def wait_for_white_color():
    detected = wait_for_color(Color.WHITE)
    return detected

async def run_detect_color():
    print("running detect color")
    await wait(0)
    HUB.light.on(Color.YELLOW)
    await HUB.speaker.beep(500, 400)
    print("prior to entering wait for color")
    detected = await wait_for_color(Color.WHITE)
    print("detected: ", detected)
    if detected:
        await subtask_play_star_wars()

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
        run_detect_color()
    )

#run_task(main())

if __name__ == "__main__":
    print("program has started!")
    run_task(main())