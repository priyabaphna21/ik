import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#link lengths
a1=a2=2.0

#eef position
x2=-0.04
y2=2.78
r=sqrt(x2**2+y2**2)
phi1=arccos((a2**2-a1**2-r**2)/(-2*a1*r))
phi2=arctan(y2/x2)
phi3=arccos((r**2-a1**2-a2**2)/(-2*a1*a2))

#joint angles
T2=pi-phi3
T1=phi2-phi1

print("T1 ")
print(T1)
print("T2 ")
print(T2)