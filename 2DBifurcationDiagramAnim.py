import numpy as np
import matplotlib.pyplot as plt


# Defines the dynamical system we are stydying
def Z(x,y,eps=5,ni=0.2,r=2):
  mu = (1-np.e**(-r))/r
  rx = x + ni*(1+mu*y) + eps*ni*mu*np.cos(2*np.pi*x)
  ry = np.e**(-r)*(y+eps*np.cos(2*np.pi*x))
  return rx%1,ry

fig, ax = plt.subplots(figsize=(8,4)) # Create as many subplots as you want

xmin, xmax, ymin, ymax = 0.1, 0.6, 0., 1.
    
ax.set_xlim((xmin, xmax)) # Set the limits of the axis of your graph    
ax.set_ylim((ymin, ymax)) # x axis will be the parameter, y axis will be the map


plt.title('Bifurcation Zaslavskii Map')# Title of the figure

plt.xlabel(r'$\nu$')    # Labels of the axis of the figure
plt.ylabel(r'$x_{n}$')  


line1, = ax.plot([], [], '.k', ms=2)     # Set the plots for the figure
line2, = ax.plot([], [], '.b', ms=2)

# Defines the space of initial conditions for the map
x = np.linspace(0, 1, 82) 
y = np.linspace(-1, 2, 22)
# Create a mesh-grid of these arrays
X, Y = np.meshgrid(x, y)

# Returns them to the shape of array
X = X.reshape((np.prod(X.shape),))
Y = Y.reshape((np.prod(Y.shape),))



NU = np.linspace(xmin, xmax, 282) # array of the parameters
# Dictionaries where we are going to iterate in the animation
# Parameter is the key, map is the value
SpaceX = {}
SpaceY = {}
for a in NU:
  SpaceX[a] = X
  SpaceY[a] = Y


# Defines the animation step
def drawframe(n):
    global SpaceX,SpaceY 
    X =[]
    Y = []
    for a in SpaceX.keys():
      # Don't iterate in the first frame  
      if n != 0:
        # Iteration of the map  
        SpaceX[a], SpaceY[a] = Z(SpaceX[a],SpaceY[a],eps=5,ni=a,r=2)
      # Joins the parametres for plotting  
      X = np.concatenate((X, a*np.ones(len(SpaceX[a]))))
      # Joins the map for plotting
      Y = np.concatenate((Y, SpaceX[a]))
    line1.set_data(X,Y)
    return (line1,line2)

from matplotlib import animation

# animates using drawframe as step
anim = animation.FuncAnimation(fig, drawframe, frames=120, interval=100, save_count=12000, blit=True)


# Saves animation as an mp4 in direction f
f = r"D:\Trabalho\Git\GitAnim\animation.mp4" 
writermp4 = animation.FFMpegWriter(fps=10) 
anim.save(f, writer=writermp4)