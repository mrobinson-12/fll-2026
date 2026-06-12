'''
This is the master program which runs each individual mission or group of missions. You should start by
importing your mission files below and then adding them to the menu list. You can add as many options
as you would like and the menu does not need to be numerical, it can be letters or special characters
as well.
'''
import mission_1_example, mission_2_example

from base_robot import *

br = BaseRobot()

from pybricks.tools import hub_menu

# Feel free to add more options to the menu and import more missions as needed.

while True:
    mission = hub_menu("1", "2", "3")

    if mission == "1":
        br.beep()
        mission_1_example.Run(br)
    elif mission == "2":
        br.beep()
        mission_2_example.Run(br)
    elif mission == "3":
        br.beep()
        pass

