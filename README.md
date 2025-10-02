# FLL-2025-2026
Starter Code for  Pybricks/FLL

Github url: https://github.com/infiniteroboticsteam/FLL-2025-2026

# Set up the hub
* Connect your hub to your computer via cable.
* GO to https://code.pybricks.com/, click "Install Pybricks Firmware" on the left and follow the intructions to install pybricks firmware on your hub.
* You can use the web interface to write code and control the hub

Below are the instructions to use vscode for programming with pybricks

# Set up github
* Download (https://desktop.github.com/download/) and install github
* Log in to github with your google gmail account and create a github account.
* In github cmd (windows), set up user.name and user.email like below: 
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

# Change in powershell

* Open powershell as an admin, type "Set-ExecutionPolicy Unrestricted -Force"
This is needed otherwise vscode cannot open the venv.

# Install python

* Download (https://www.python.org/downloads/) and install python

# Set up vscode 

* Download (https://code.visualstudio.com/download) and install visual studio code. In vscode, 
* Install the following extensions: pylance, python
* In command, type "py create env" and select "Python: Create Environment..." to create a virtual environment
* In command, type "py create term" and select "Python: Create Terminal". In the terminal, type: pip install pybricks pybricksdev
* Click "source control" on the left, and clone our team repo: https://github.com/infiniteroboticsteam/FLL-2025-2026. Then you should have downloaded the repo in your local computer. 
* Click "Explorer" to go back to view the files. Go to .vscode/launch.json and change "infinite-1" to the name of your hub.
* Click "run_demo.py", review the code and Press F5 to do a test run.


# code structure

1. the parameters for our driving base and sensor ports are in robot_config.py

2. Use run_demo.py as an example on how to write the code for a run.

    A run is defined as a procedure where the driving base with attachments installed starts from a launch area and returns to either a home area or a launch area. 

    A run can be programed to complete multiple missions.

3. Steps to write your code for a run.
    
    * For each mission, define a function to move the each attachment to complete a mission.
    * define a function to move the driving base, at approporiate waypoint (based on distance), add movements for attachments.
    * test the function for a run in your run.

4. At the end, we will use robot.py to add all runs to the program so that during the competition we run different runs by pressing buttons on the hub. Remember, laptop/ipad are not allowed in the game.


# Use git to upload your code for missions

TODO

* If you changed the name in launch.json, do not add the json file in your commit.


# Credits

* The original repo was forked from https://github.com/MonongahelaCryptidCooperative/FLL-2025-2026.
* Thanks to Boyd Fletcher for sharing his experience using pybricks.
* Original guide to set up vscode for pybricks: https://pybricks.com/project/pybricks-other-editors/
