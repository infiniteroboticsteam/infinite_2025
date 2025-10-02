from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

# Set up all devices.
HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.X)

DRIVE_LEFT = Motor(Port.B, Direction.COUNTERCLOCKWISE)
DRIVE_RIGHT = Motor(Port.F, Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, 56, 114)

CENTER_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)

#LEFT_COLOR_SENSOR = ColorSensor(Port.A)
#RIGHT_COLOR_SENSOR = ColorSensor(Port.E)

#LEFT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)
#RIGHT_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)

# Initialize variables.
SPEED = 621
ACCELERATION = 600
TURN_SPEED = 400
TURN_ACCELERATION = 1000

# for teleop
MANUAL_MOTOR_SPEED = 250
TELEOP_SPEED = 300
TELEOP_ACCEL = 1000
TELEOP_TURN = 200
TELEOP_TURN_ACCEL = 1000
TELEOP_ATTACH_SPEED = 600
# Change to match the setup of your robot. Adjust speeds as necessary
