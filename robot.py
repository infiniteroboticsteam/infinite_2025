from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from text_library import print_drivebase_settings
#from measurements import left_attach_measurements, push_measurements, right_attach_measurements
from ui import add_program, user_interface

from run_demo import run1
from text_example import run2

async def main():
    # Import from xbox_teleop the teleop function if you want to use
    # the telop mode and add the telop program
    # Must be paired at starup or will crash. Disconnect block if not wanted
    # Note the code is provided disconnected.

    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )
    # Print to consule the default drivebase settings
    await print_drivebase_settings()
    # Override these settings. Note pybricks is conservative with speeds.
    # The default speeds are about 40% of what the motors can handle
    # You probably can double the default speeds in the robot_config file.
    # Conversely the accelration values pybricks creates tend to be too high
    # If your wheels slip your distances will be off. Lower accelration as needed
    # in the robot_config file to eliminate wheel slippage. These values will depend on wheel choice, center of gravity of your robot and robot weight.
    await set_drivebase()
    # Add the programs (Missons) below they will appear in the order placed
    # Missions will need to be imported, see example missions/utility programs
    # below
    await add_program(run1, '1', Color.GREEN)
    #await add_program(push_measurements, 'P', Color.BLUE)
    #await add_program(left_attach_measurements, 'L', Color.BLUE)
    #await add_program(right_attach_measurements, 'R', Color.BLUE)
    await add_program(run2, '2', Color.RED)
    # Launch the user interface
    await user_interface()


if __name__ == "__main__":
    run_task(main())