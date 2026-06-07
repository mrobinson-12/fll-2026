# Ignore this, this just imports the BaseRobot class, which has the funtions for the robot
# Test script for testing the new functions I make, will be deleted soon.
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=600, distance=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=300, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=500)




















# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
