from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

#this class allows to change the gear configuration of a motor
#without creating a new motor object
class GearSwapMotor(Motor):
    def __init__(self, port):
        self.port = port
        self.reconfigure(Direction.CLOCKWISE, None)

    def reconfigure(self, positive_direction, gears):
        super().__init__(self.port, positive_direction, gears)

# Initialize variables.
SPEED = 500
ACCELERATION = 500
TURN_SPEED = 300
TURN_ACCELERATION = 300

# Set up the drive base.
DRIVE_LEFT = Motor(Port.B, Direction.COUNTERCLOCKWISE)
DRIVE_RIGHT = Motor(Port.F, Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, 56, 114)

# set up the attachments, if needed
#CENTER_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)
CENTER_ATTACHMENT = GearSwapMotor(Port.D)

# default configuration: clockwise, no gears
# you can change the configuration in your program, e.g.,
# CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])
# after chaning he configuration, you may want to reset the angle
# CENTER_ATTACHMENT.reset_angle(0)


#if you need color sensors, uncomment the following lines
#LEFT_COLOR_SENSOR = ColorSensor(Port.A)
#RIGHT_COLOR_SENSOR = ColorSensor(Port.E)


# Set up all devices.
HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
