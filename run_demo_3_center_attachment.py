from pybricks.parameters import Color
from pybricks.tools import run_task, wait

from robot_config import HUB, CENTER_ATTACHMENT

#this function tests control of center attachment.
async def demo_center_attachment():
    await HUB.speaker.beep()
    # for precision control, reset angle at the beginning.
    # this function set the counter to be 0, 
    # but not the absolute location (recall the markers on the motor and driving wheel)
    CENTER_ATTACHMENT.reset_angle(0)
    await CENTER_ATTACHMENT.run_angle(180, 360) #speed, angle
    await wait(2000)
    await CENTER_ATTACHMENT.run_angle(180, -360) 

    #repeat small movements
    for i in range(5):
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(180, 90) 
        await wait(500)
        await CENTER_ATTACHMENT.run_angle(180, -90)
 

if __name__ == "__main__":
    run_task(demo_center_attachment())