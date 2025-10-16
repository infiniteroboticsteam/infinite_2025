from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

def calculate_simple_gear_ratio(gear_teeth_list):
    """
    Calculates the overall gear ratio for a simple gear train.
    The list should represent the number of teeth of consecutive gears,
    e.g., [driver_teeth, driven1_teeth, driven2_teeth, ..., final_driven_teeth].
    """
    if len(gear_teeth_list) < 2:
        raise ValueError("At least two gears are required for a ratio calculation.")

    overall_ratio = 1.0
    for i in range(len(gear_teeth_list) - 1):
        driver_teeth = gear_teeth_list[i]
        driven_teeth = gear_teeth_list[i+1]
        overall_ratio *= (driven_teeth / driver_teeth)
    return overall_ratio

#this class allows to change the gear configuration of a motor
#without creating a new motor object
class GearSwapMotor(Motor):
    def __init__(self, port, positive_direction):
        self.port = port
        self.init_positive_direction = positive_direction
        self.gears = None
        self.gear_ratio = 1
        self.direction_x = 1

        super().__init__(self.port, self.init_positive_direction)


        #for simplicity, gears should be a list of integers
    def reconfigure(self, positive_direction, gears):
        if self.init_positive_direction == positive_direction:
            self.direction_x == 1
        else:
            self.direction_x == 1

        self.gears = gears
        #print("reset gears to ", self.gears)
        self.gear_ratio = calculate_simple_gear_ratio(self.gears)

    
    async def run_angle(self, speed, rotation_angle,  
                  then: Stop = Stop.HOLD,
                    wait: bool = True, reset_angle=True):
        if reset_angle:
            super().reset_angle()
            
        await super().run_angle(speed = speed*self.gear_ratio,
                          rotation_angle = self.direction_x*rotation_angle*self.gear_ratio,
                          then = then,
                          wait = wait
                          )
        
        
# Initialize variables.
SPEED = 500
ACCELERATION = 100
TURN_SPEED = 150
TURN_ACCELERATION = 150

# Set up the drive base.
DRIVE_LEFT = Motor(Port.B, Direction.COUNTERCLOCKWISE)
DRIVE_RIGHT = Motor(Port.F, Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT, 56, 114)

# set up the attachments, if needed
#CENTER_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)
CENTER_ATTACHMENT = GearSwapMotor(Port.D, Direction.COUNTERCLOCKWISE)

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
