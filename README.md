# Overview
Project Files For Final year Project - Control for Traffic Light System in Large Roundabouts with reinforcement Learning.
This project utilizes the SUMO simulation package to simulate traffic environments using Deep Q-Learning Traffic Control Agents.


# Contents

## net directory contains .xml files for traffic environments
## result directory contains .csv and .png files of simulation results
## routes directory contains .xml files for traffic demand elements
## scripts directory contains scripts used in the project. Tools directory includes the plot.py and randomTrips.py scripts which are provided by the SUMO-RL library and SUMO software respectively.


# Setting up (Windows 10)

1. install virtualenv with pip install virtualenv
2. CD to capstone_project2
3. run command $ Scripts\active
4. CD to simulator/scripts
5. run scripts of choice e.g. $ python main.py
5.run command $ deactivate
	to deactivate virtual environment



# Commands

## Command to run the randomTrips.py file:
python randomTrips.py -n <XML_FILE> -e <TOTAL_TIMESTEPS> --binomial <VEHICLE_SPAWN_AMOUNT> --fringe-factor <MAX> --period <FLOAT>

## Command to run the plot.py file:
python plot.py -f <CSV_FILE> -ma <FLOAT>
