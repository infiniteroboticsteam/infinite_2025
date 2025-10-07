from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

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
CENTER_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)

#if you need color sensors, uncomment the following lines
#LEFT_COLOR_SENSOR = ColorSensor(Port.A)
#RIGHT_COLOR_SENSOR = ColorSensor(Port.E)


# Set up all devices.
HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
