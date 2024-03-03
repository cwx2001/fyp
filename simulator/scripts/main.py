# -*- coding: utf-8 -*-
"""
Created on Mon May 15 00:12:09 2023

@author: User
"""

import os, sys
import gymnasium as gym
sys.modules["gym"] = gym

from sumo_rl import SumoEnvironment
from stable_baselines3.dqn.dqn import DQN


if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
    
    
sumoBinary = os.environ['SUMO_HOME'] + 'bin\sumo-gui.exe'
sumoCmd = [sumoBinary, "-c", "roundaboutRoute.sumocfg"]



###
# net_file
#
# new_rltl_roundabout.net.xml
# notl_roundabout.net.xml
#
# subang_rltl_roundabout.net.xml
# subang_notl_roundabout.net.xml
#
###

###
#
# set min_green = max_green for fixed TLS setup (40)
#
#
# fixed value = 40
# min value = 6
# max value = 60
#
#
# IRL values
# fixed value = 90
# min value = 30
# max value = 120
#
#
###

###
# default yellow time = 2
# default delta time = 5
###

###
# subang yellow time = 6
# subang delta time = 10
###


if __name__ == "__main__":
    env = SumoEnvironment(
        net_file="../net/subang/subang_rltl_roundabout.net.xml",
        route_file="../routes/subang/subang_normal.rou.xml",
        out_csv_name="../result/demonstration/demo_result",
        single_agent=True,
        use_gui=True,
        num_seconds=1000,
        yellow_time=6,
        delta_time=10,
        min_green=30,
        max_green=120,
        )
    
    model = DQN(
        env=env,
        policy="MlpPolicy",
        learning_rate=0.001,
        learning_starts=0,
        train_freq=1,
        target_update_interval=500,
        exploration_initial_eps=1,
        exploration_final_eps=0.01,
        verbose=1,
        )
    
    # ts = env.traffic_signals["J0"]
    # print(ts.lanes)
    
    
    #default timestep = 100,000
    model.learn(total_timesteps=1000, progress_bar=False)

    