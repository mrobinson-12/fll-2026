# Documentation on PyBricks

### What commands mean:
***
#### driveForDistance()
This command drives forward for the distance you set and is formatted like this. driveForDistance(distance, speed, then, gyro). Distance is in mm. Speed is in mm/s. For then, see https://docs.pybricks.com/en/latest/parameters/stop.html#pybricks.parameters.Stop for more information but you can either do Stop.BRAKE, Stop.COAST, Stop.HOLD, or STOP.NONE. There are other options but these will be the main ones you will use. Lastly, the gyro setting is for if you want it to correct itself while it is moving e.g. if it moves off track.
#### turn()
This command turns the specified amount of degrees set. It is formatted like this turn(angle, speed, then, gyro). Angle is in degrees. Speed is in degrees/s. For then, see https://docs.pybricks.com/en/latest/parameters/stop.html#pybricks.parameters.Stop for more information but you can either do Stop.BRAKE, Stop.COAST, Stop.HOLD, or STOP.NONE. There are other options but these will be the main ones you will use. Lastly, the gyro setting is for if you want it to correct itself while it is moving e.g. if it moves off track.
#### lightOn()
This command turns the light on on the centre button of the SPIKE Prime Hub. It is formatted like lightOn(h, s, v), you will need to put in the HSV values for colours.
#### lightOff()
Turns the light off!
#### wait()
Waits for the amount of ms provided. E.g. wait(1000) would be 1 second. 
#### move[Left/Right]AttachmentMotorForMillis()
Moves the selected motor for the milliseconds provided. It is formatted like moveLeftAttachmentMotorForMillis(millis, speed)
#### move[Left/Right]AttachmentMotorForDeg()
Moves the selected motor at the angle provided. It is formatted like moveLeftAttachmentMotorForDeg(deg, speed)
