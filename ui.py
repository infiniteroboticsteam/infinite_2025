"""
User Interface for Pybricks FLL
"""

from pybricks.parameters import Color, Button, Side
from robot_config import HUB
from pybricks.tools import multitask, wait

ACTIVE_PROGRAM = 0
PROGRAM_LIST = list()


class RobotProgram(object):
    """ A class that holds our RobotPrograms. RobotPrograms have a method
    that is called when a program is launched. Also has as single character that,
    if the robot has a display, will be displayed as well as a color attribute
    that will change the color of the light on the hub. This is used to match the
    color of attachments to the color of the program and provides an additional
    cue to ensure the correct attachements are placed on the robot"""
    def __init__(
        self,
        func:callable,
        character:chr = "E",
        light_color:Color = Color.BLUE):

        self.label:chr = character
        self.color:Color = light_color 
        self.function:callable = func




async def flip_screen():
    HUB.display.orientation(Side.BOTTOM)


async def next_program():
    """Selects the next Program"""
    global ACTIVE_PROGRAM, PROGRAM_LIST
    ACTIVE_PROGRAM = (ACTIVE_PROGRAM + 1) % len(PROGRAM_LIST)

async def prior_program():
    """Selects the prior program"""
    global ACTIVE_PROGRAM, PROGRAM_LIST
    ACTIVE_PROGRAM = (ACTIVE_PROGRAM - 1) % len(PROGRAM_LIST)


async def add_program(func:callable, char:chr = "E", color:Color = Color.BLUE):
    """ Adds a RobotProgram object to the PROGRAM_LIST"""
    PROGRAM_LIST.append(RobotProgram(func, char, color))

async def update_display():
    """Updates the Hub display with the character and button color"""
    current_program = PROGRAM_LIST[ACTIVE_PROGRAM]
    HUB.display.char(current_program.label)
    HUB.light.on(current_program.color)

async def user_interface():
    """
    Main user interface code. Iterates through a program list with the
    left/right buttons"""
    # Hold center button to stop
    HUB.system.set_stop_button(None) #Button.CENTER)
    # Main loop/interface that allows for selecting and launching programs
    while True:
        buttons = HUB.buttons.pressed()
        # Check to see if the gyro is ready, if not display E/red button
        if HUB.imu.ready():
            # Display the active program/color
            await update_display()
            # Check Buttons
            if Button.LEFT in buttons:
                # The left side button goes back to the previous program
                await prior_program()
                await update_display()
                await HUB.speaker.beep(500, 200)
            elif Button.RIGHT in buttons:
                # The right side  button advances to the next program
                await next_program()
                await update_display()
                await HUB.speaker.beep(500, 200)
            elif Button.CENTER in buttons:
                # The center button launches the currently selected program
                await PROGRAM_LIST[ACTIVE_PROGRAM].function()
            else:
                await wait(10)
        else:
            # If Hub is not ready display an E for Error and wait until hub is ready
            # Place on flat surface to calibrate gyro/remove error state
            HUB.light.on(Color.RED)
            HUB.display.char('E')
            await wait(10)
    