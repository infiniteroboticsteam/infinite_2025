from pybricks.tools import multitask, run_task, wait
from robot_config import CENTER_ATTACHMENT, DRIVE_BASE, FRONT_ATTACHMENT
from library import set_drivebase

async def run3():
    print("running run 3")
    await set_drivebase()
    DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-706.7)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-125)
    await DRIVE_BASE.turn(-15)
    await FRONT_ATTACHMENT.run_angle(9999, 1500)
    await DRIVE_BASE.turn(15)
    await DRIVE_BASE.straight(150)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(-650)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-161)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(121)
    await CENTER_ATTACHMENT.run_angle(500, 75.67416741674167416741674167416741674167416741)
    await wait(500)
    await DRIVE_BASE.straight(-60)
    await CENTER_ATTACHMENT.run_angle(500, -75.67416741674167416741674167416741674167416741)
    await DRIVE_BASE.straight(254)
    await wait(500)
    await DRIVE_BASE.straight(-630)
    #await DRIVE_BASE.stop()
    DRIVE_BASE.use_gyro(False) 
  


if __name__ == "__main__":
    run_task(run3())