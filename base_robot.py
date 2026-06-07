from pybricks.pupdevices import Motor, ColorSensor

from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks import version


# TODO: THESE ARE EXAMPLE VALUES!
TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm
COLOR_SENSOR_PORT = Port.F
COLOR_SENSOR_PORT_2 = Port.B
LEFT_DRIVE_MOTOR_PORT = Port.E
RIGHT_DRIVE_MOTOR_PORT = Port.A
LEFT_ATTACHMENT_MOTOR_PORT = Port.C
RIGHT_ATTACHMENT_MOTOR_PORT = Port.D

# Check the pybricks API documentation to see how these parameters are set
# and used. Add other parameters that your robot needs.
class BaseRobot:

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        self.leftDriveMotor = Motor(LEFT_DRIVE_MOTOR_PORT, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(RIGHT_DRIVE_MOTOR_PORT, Direction.CLOCKWISE)
        self.robot = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )

        self.leftAttachmentMotor = Motor(LEFT_ATTACHMENT_MOTOR_PORT)
        self.rightAttachmentMotor = Motor(RIGHT_ATTACHMENT_MOTOR_PORT)

        self.colorSensor = ColorSensor(COLOR_SENSOR_PORT)
        self.colorSensor2 = ColorSensor(COLOR_SENSOR_PORT_2)



# Millis*, Speed*
# Confirmed working
    def moveLeftAttachmentMotorForMillis(
        self,
        millis,
        speed,
    ):
        self.leftAttachmentMotor.run_time(speed, millis)


# Params: Distance*, Speed*, Then, Gyro
# Confirmed working
    def driveForDistance(
        self,
        distance,
        speed,
        then=Stop.BRAKE,
        gyro=True,
    ):
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_speed=speed)
        self.robot.straight(distance, then, wait)

# Params: Angle*, Speed*, Then, Gyro
# Confirmed working
    def turn(
        self,
        angle,
        speed,
        then=Stop.BRAKE,
        gyro=True,
    ):
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_speed=speed)
        self.robot.turn(angle, then, wait)




if __name__ == "__main__":
    print("Don't run the BaseRobot class file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
