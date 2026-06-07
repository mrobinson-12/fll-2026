'''
This code should not need to be run directly or edited by the students. It is a baserobot class which includes functions, settings, and setup for the robot.
There are variables in here that should be changed to match the configuration of your robot and you can add some extra functions if you would like.
'''
from pybricks.parameters import Color
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.tools import wait

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


# THESE MUST BE CHANGED TO MATCH YOUR ROBOT'S CONFIGURATION
TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm
COLOR_SENSOR_PORT = Port.F
COLOR_SENSOR_PORT_2 = Port.B
LEFT_DRIVE_MOTOR_PORT = Port.E
RIGHT_DRIVE_MOTOR_PORT = Port.A
LEFT_ATTACHMENT_MOTOR_PORT = Port.C
RIGHT_ATTACHMENT_MOTOR_PORT = Port.D


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
        




    def moveLeftAttachmentMotorForMillis(
        self,
        millis,
        speed,
    ):
        self.leftAttachmentMotor.run_time(speed, millis)

    def moveRightAttachmentMotorForMillis(
        self,
        millis,
        speed,
    ):
        self.rightAttachmentMotor.run_time(speed, millis)

    def moveLeftAttachmentMotorForDeg(
        self,
        degrees,
        speed,
    ):
        self.leftAttachmentMotor.run_angle(speed, degrees, then=Stop.BRAKE, wait=True)

    def moveRightAttachmentMotorForDeg(
        self,
        degrees,
        speed,
    ):
        self.rightAttachmentMotor.run_angle(speed, degrees, then=Stop.BRAKE, wait=True)

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

    def lightOn(
        self,
        h,
        s,
        v,
        color=None,
    ):
        self.hub.light.on(Color(h, s, v))

    def wait(
        self,
        time,
    ):
        wait(time)

    def lightOff(
        self
    ):
        self.hub.light.off()

    def beep(
        self,
    ):
        self.hub.speaker.beep()

    def resetHeading(
        self,
        angle=0,
    ):
        self.robot.reset_heading(angle)




if __name__ == "__main__":
    print("Don't run the BaseRobot class file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
