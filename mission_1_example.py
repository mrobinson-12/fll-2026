# Ignore this, this just imports the BaseRobot class, which has the funtions for the robot
# Test script for testing the new functions I make, will be deleted
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=300, distance=600, then=Stop.BRAKE, gyro=True)






















# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
