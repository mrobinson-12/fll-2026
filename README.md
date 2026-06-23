# Pybricks & VS Code

This is a template for a Pybricks and VS Code setup for FIRST LEGO League Challenge teams to use in the 2026-2027 season, "BioGlow". Our team has decided to use Pybricks this year for programming our Spike PRIME robots. I have to give lots of credit to [Skip Morrow](https://github.com/MrGibbage) for the guides on using Pybricks and VS Code. This is a fork of [His template repo](https://github.com/MrGibbage/pybricks-fll) which I have decided to add quite a bit to and make it easier to understand and use for new teams like us who are using Pybricks and python for the first time as well. I've noticed in the repo's that Skip Morrow uses for his teams, they are quite complicated for students who are just learning python, but the base repo he provides doesnt give too much info about how to use it.

Some things I have added (or are planning to add) are:

- A .gitignore file.
- Installation scripts for MacOS (Finished), and Windows (In Progress), with Arch and Ubuntu supported (untested atm)
- A space for innovation project research and a template for notes that fit with the judging criteria.
- More functions in the base_robot.py class to be used.
- Pybricks runner extension reccomendation
- In depth documentation on how to use the repo (Coming soon).
- Integration with Hackatime in the install script (Linux & MacOS Only).
- PyBricks coding AI agent (In progress).
- Hopefully clearer comments which are easier to understand.
- Resources and lessons for teaching students Pybricks and Python.
- Add calibration scripts (In progress).

Feel free to contribute! It would be greatly appreciated!

### Setup

1. Install VS Code from https://code.visualstudio.com/download?_exp_download=fb315fc982
2. Make sure you have access to the repo you are cloning from if you are using someone elses
2. Download the install script for your OS from the help/install directory and run the script
3. Get a classic GitHub token with the repo scope https://github.com/settings/tokens
4. When asked, enter your token in the script. It is not saved and is only used once for cloning the repo
4. Flash the pybricks firmware to your spike prime robot from https://code.pybricks.com in the settings menu
5. Open VS Code and then open the folder created by the script
6. Log into GitHub in VS code
7. Open the venv in vs code in terminal with the command for your OS
8. Edit the values on base_robot.py to fit your robot 
9. Make sure the Pybricks Runner extension is installed
9. Run mission_1_example.py with 'pybricksdev run ble --name "[Robot name]" "mission_1_example.py"'
10. For more info about commands and functions, go to the help/docs folder for more info!
