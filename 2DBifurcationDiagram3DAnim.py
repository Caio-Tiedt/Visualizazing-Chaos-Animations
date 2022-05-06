import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

# Defines the dynamical system we are stydying
def Zel(x,y,eps=5,ni=0.2,r=2):
  mu = (1-np.e**(-r))/r
  rx = x + ni*(1+mu*y) + eps*ni*mu*np.cos(2*np.pi*x)
  ry = np.e**(-r)*(y+eps*np.cos(2*np.pi*x))
  return rx%1,ry

rot=True # Sets if you want your animation rotating or not
l=180 # Sets the number of frames in your animation

fig = plt.figure()
ax = p3.Axes3D(fig)  # Create as many subplots as you want, here a 3d plot

minX, maxX, minY, maxY = 0.1, 0.6, 0., 1.
minZ, maxZ = -1, 2

ax.set_xlim((minX, maxX))            
ax.set_ylim((minY, maxY))
ax.set_zlim3d([minZ, maxZ])

plt.title('Bifurcation Zaslavskii Map')# Title of the figure


plt.xlabel(r'$\nu$')
plt.ylabel(r'$x_{n}$')
ax.set_zlabel(r'$y_{n}$')

# Defines the space of initial conditions for the map
x = np.linspace(0, 1, 82) 
y = np.linspace(-1, 2, 22)
# Create a mesh-grid of these arrays
X, Y = np.meshgrid(x, y)

# Returns them to the shape of array
X = X.reshape((np.prod(X.shape),))
Y = Y.reshape((np.prod(Y.shape),))


NU = np.linspace(minX, maxX, 162) # array of the parameters
# Dictionaries where we are going to iterate in the animation
# Parameter is the key, map is the value
SpaceX = {}
SpaceY = {}
for a in NU:
  SpaceX[a] = X
  SpaceY[a] = Y


# Generates the data that will be animated
def BifDia(length=100): 
    global SpaceX,SpaceY
    TimeX={}
    TimeY={}
    TimeZ={}
    for i in range(length):
      X = []
      Y = []
      Z = []
      for a in SpaceX.keys():
        if i != 0:
          SpaceX[a], SpaceY[a] = Zel( SpaceX[a], SpaceY[a],eps=5,ni=a,r=2)
        X = np.concatenate((X, a*np.ones(len(SpaceX[a]))))
        Y = np.concatenate((Y, SpaceX[a]))
        Z = np.concatenate((Z, SpaceY[a]))
      TimeX[i] = X       
      TimeY[i] = Y
      TimeZ[i] = Z   
    return TimeX,TimeY,TimeZ

TimeX,TimeY,TimeZ=BifDia(l)


line, = ax.plot([], [], [], '.k', ms=2)

# animation function. This is called sequentially
def drawframe(i, line, TimeX, TimeY, TimeZ):
    line.set_data(TimeX[i], TimeY[i])
    line.set_3d_properties(TimeZ[i])
    if rot:
      ax.view_init(azim=2*i)
    return (line,)

from matplotlib import animation

# animates using drawframe as step
anim = animation.FuncAnimation(fig, drawframe, fargs=(line,  TimeX,  TimeY,  TimeZ), frames=l, interval=100, blit=True)

# Saves animation as an mp4 in direction f
f = r"D:\Trabalho\Git\GitAnim\animation.mp4" 
writermp4 = animation.FFMpegWriter(fps=10) 
anim.save(f, writer=writermp4)