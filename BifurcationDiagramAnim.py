# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:56:14 2022

@author: caio_
"""

import numpy as np
import matplotlib.pyplot as plt


def flog(a,x): # Defines the dynamical system we are stydying
  x1 = a * x
  x2 = ( 1 - x )
  return np.multiply(x1, x2)

fig, ax = plt.subplots(figsize=(8,4)) # Create as many subplots as you want

xmin, xmax, ymin, ymax = 2., 4., 0., 1.
    
ax.set_xlim((xmin, xmax)) # Set the limits of the axis of your graph    
ax.set_ylim((ymin, ymax)) # x axis will be the parameter, y axis will be the map

plt.title('Bifurcation Logistic Map') # Title of the figure

plt.xlabel('a') # Labels of the axis of the figure
plt.ylabel(r'$x_{n}$')

line1, = ax.plot([], [], '.k', ms=2)     # Set the plots for the figure
line2, = ax.plot([], [], '.b', ms=2)


X = np.linspace(ymin, ymax, 301) # Sets the starting values of the map
A = np.linspace(xmin, xmax, 152) # Sets the values of the parameters

Space = {}  # A dictionary where we are going to iterate in the animation

for a in A: # Parameter is the key, map is the value
  Space[a] = X


def drawframe(n): # Defines the animation step
    global Space
    X =[]
    Y = []
    for a in Space.keys():
      if n != 0:    # Don't iterate in the first frame
        Space[a] = flog(a,Space[a]) # Iteration of the map
      X = np.concatenate((X, a*np.ones(len(Space[a])))) # Joins the parametres for plotting
      Y = np.concatenate((Y, Space[a]))  # Joins the map for plotting
    line1.set_data(X,Y) # Plots
    return (line1,line2)

from matplotlib import animation

# animates using drawframe as step
anim = animation.FuncAnimation(fig, drawframe, frames=120, interval=100, save_count=12000, blit=True)


# Saves animation as an mp4 in direction f
f = r"D:\Trabalho\Git\GitAnim\animation.mp4" 
writermp4 = animation.FFMpegWriter(fps=10) 
anim.save(f, writer=writermp4)