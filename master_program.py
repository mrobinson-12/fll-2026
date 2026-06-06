from base_robot import *

# Import missions
import sample_mission1, sample_mission2


br = BaseRobot()

pressed = br.hub.buttons.pressed()

# here's one way to create a master program. There are many other ways to do
# it, but that is up to the team.
# For example, here's another way: 
# https://pybricks.com/prop1@:#####################################################################################################################################"ject/spike-hub-menu/

# Here, we just wait until a button is pressed before starting the mission
while Button.LEFT not in pressed:
    pressed = br.hub.buttons.pressed()

sample_mission1.Run(br)

# presumably the robot returned to base, and you have now configured it to
# run the next mission. In any case, when sample_mission1 is done running
# the robot goes again into the loop to wait for the button press. This
# time we will run the sample_mission2 program

while Button.LEFT not in pressed:
    pressed = br.hub.buttons.pressed()

sample_mission2.Run(br)
