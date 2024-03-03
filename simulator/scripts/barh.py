# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:04:20 2023

@author: User
"""

import pandas as pd
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

import matplotlib.pyplot as plt

# control_schemes = ["Fixed-Time", "RL", "No TSC"]
control_schemes = ["Fixed-Time", "RL"]

# Define values of simulation results
normal_values = (25158825 , 16696997 , 172038)
dense_values = (210634972 , 136048046)
biased_values = (67587913 , 25957084 , 18013)

subang_normal_values = (24906133 , 10160415, 19396)
subang_dense_values = (83447831 , 30849119)

def horizontal_bar_plot(name, values, title):
        # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9))
    
    # Horizontal Bar Plot
    ax.barh(name, values)
    
    # Remove spines on axes
    for s in ['top', 'bottom', 'left', 'right']:
    	ax.spines[s].set_visible(False)

    
    # Set padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    
    
    # Add gridlines
    ax.grid(b = True, color ='grey',
    		linestyle ='-.', linewidth = 0.5,
    		alpha = 0.2)
    
    # Invert axis
    ax.invert_yaxis()
    
    # Annotation
    for i in ax.patches:
    	plt.text(i.get_width()+0.2, i.get_y()+0.5,
    			str(round((i.get_width()), 2)),
    			fontsize = 10, fontweight ='bold',
    			color ='grey')
    
    # Add Plot Title
    ax.set_title(title,
    			loc ='center', )
    
    ax.set_xlabel("Accumulative Total Waiting Time  (seconds)")
    ax.set_ylabel("Traffic Signal Control Scheme")
    
    
    # Show Plot
    plt.show()
    pass



if __name__ == "__main__":
    horizontal_bar_plot(control_schemes, dense_values, "Accumulative Total Waiting Time of Traffic Controllers in Normal Condition")


