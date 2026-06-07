# Menu to select missions
from base_robot import *
br = BaseRobot()
from pybricks.tools import hub_menu
# Import missions
import mission_1_example, mission_2_example
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

