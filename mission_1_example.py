# Ignore this, this just imports the BaseRobot class, which has the funtions for the robot
# Test script for testing the new functions I make, will be deleted
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=600, distance=500, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=400, then=Stop.BRAKE, gyro=True)
    br.lightOn(h=0, s=100, v=100)
    br.wait(1000)
    br.lightOff()
    br.moveLeftAttachmentMotorForDeg(degrees=90, speed=400)
    br.turn(angle=90, speed=400, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=400, distance=300, then=Stop.COAST, gyro=True)




















# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
