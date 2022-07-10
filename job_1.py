from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
# change the variables x and y to any thing
x = 0
y = 0
# make subplot of 2 * 2 
fig, axs = plt.subplots(2, 2)
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1]) 
# set the background color
#plt.ylabel("y-axis")
#=====================Setting the background color of figure============
axs[0,0].set_facecolor("blue")
axs[0,0].scatter(x,y)
axs[0, 0].set_title('y-axis')
#=================drawing the scatter plot from dataframe ===========
axs[0, 1].scatter(x, y)
axs[0,1].set_facecolor("green")

# axs[0, 1].plot(x, y, 'tab:orange')
# axs[0,1].axis("off")
#====================setting the x-axis to empty string ===============
axs[0,0].set_xticklabels([])
axs[0,0].set_yticklabels([])

axs[0,1].set_xticklabels([])
axs[0,1].set_yticklabels([])
axs[1,1].set_yticklabels([])
axs[1,0].set_xticklabels([])
axs[1,0].set_yticklabels([])
axs[0,1].set_yticklabels([])
axs[0,1].set_yticklabels([])
axs[1,1].set_xticklabels([])
# axs[0, 1].set_title('check')
# axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].scatter(x, y)
axs[1,0].set_facecolor("grey")
# axs[1, 1].plot(x, -y, 'tab:red')

axs[1,1].set_facecolor("yellow")
axs[1, 1].scatter(x, y)
axs[0,0].annotate("Q2",(0.1,0.5))
axs[0,1].annotate("Q1",(0.1,0.5))
axs[1,0].annotate("Q3",(0.1,0.5))   
axs[1,1].annotate("Q4",(0.1,0.5))
#============== label the frame with first and so ...============

plt.xlabel("x-axis")

plt.plot(x,y)
plt.show()
