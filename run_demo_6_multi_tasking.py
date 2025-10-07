from pybricks.tools import run_task, wait, multitask
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor

from run_demo_3_center_attachment import demo_center_attachment 
from run_demo_1_drive_straight_turn import demo_drive_straight_turn

async def demo_multitasking():
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        demo_drive_straight_turn(),
        demo_center_attachment()
    )


if __name__ == "__main__":
    run_task(demo_multitasking())