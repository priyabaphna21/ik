import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#link lengths
a1=2.0
a2=2.0

init_x=0
init_y=0

des_x=-2
des_y=2

inc_x=0.01
inc_y=0.01

if(des_y<init_y):
    inc_y=-0.01
if(des_x<init_x):
    inc_x=-0.01

#eef position array
Y=np.arange(init_y,des_y,inc_y)
X=np.arange(init_x,des_x,inc_x)


X1 = np.zeros(len(X))
Y1 = np.zeros(len(Y)) 
X2 = np.zeros(len(X)) 
Y2 = np.zeros(len(Y))
val=len(X)
if(len(Y)>len(X)):
    val=len(Y)
    Y[len(Y):len(X)] = des_y
else:
    Y[len(X):len(Y)] = des_x

ind=np.arange(0,val,1)


for ind1,x,y in zip(ind,X,Y):

    #ik
    r=sqrt(x**2+y**2)

    if(x>=0 and y>=0):
    
        phi1=np.arccos((a1**2+r**2-a2**2)/(2*a1*r))
        phi2=np.arctan(y/(x+0.00001))
        phi3=np.arccos((a1**2+a2**2-r**2)/(2*a1*a2))

    if(x<0 and y>0):
        phi1=-np.arccos((a1**2+r**2-a2**2)/(2*a1*r))
        phi2=pi/2-np.arctan(y/(x+0.00001))
        phi3=-np.arccos((a1**2+a2**2-r**2)/(2*a1*a2))       


    #joint angles
    T1=phi1+phi2
    T2=phi3-pi


    #fk
    x1=a1*cos(T1)
    y1=a1*sin(T1)

    x2=a1*cos(T1)+a2*cos(T2+T1)
    y2=a1*sin(T1)+a2*sin(T2+T1)

    if(sqrt(x**2+y**2)>a1+a2):
        print("out of bounds")
        #pwm=0
    
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
