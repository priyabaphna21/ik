import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#link lengths
a1=a2=2.0

increment=0.1

#eef position array
y=0.0
X=np.arange(0,5,increment)

# x=2.2
# y=2.8

X1 = np.zeros(len(X))
Y1 = np.zeros(len(X)) 
X2 = np.zeros(len(X)) 
Y2 = np.zeros(len(X))

for ind1,x in enumerate(X, start=0):

  
    r=sqrt(x**2+y**2)
    phi1=np.arctan(y/x)
    phi2=np.arccos((r**2+a1**2-a2**2)/(2*r*a1))
    phi3=np.arccos((a1**2+a2**2-r**2)/(2*a1*a2))

    #joint angles
    T2=pi-phi3
    T1=phi1-phi2

    # print("T1 ")
    # print(T1)
    # print("T2 ")
    # print(T2)

    x1=a1*cos(T1)
    y1=a1*sin(T1)

    x2=a1*cos(T1)+a2*cos(T1+T2)
    y2=a1*sin(T1)+a2*sin(T1+T2)

    X1[ind1] = x1 
    Y1[ind1] = y1
    X2[ind1] = x2
    Y2[ind1] = y2 

# set up the figure and subplot
fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
ax.set_title('2-DOF animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')

# initialization function
def init():
    line.set_data([], [])
    return line,

# animation function
def animate(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]

    line.set_data(x_points, y_points)
    return line,

# call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=100, blit=True, repeat=False)
## to save animation, uncomment the line below:
## ani.save('offset_piston_motion_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#show the animation
plt.show()
    









