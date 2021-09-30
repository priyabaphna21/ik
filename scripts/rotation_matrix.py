#! /usr/bin/env python
import numpy as np
 
# if __name__ =="__main__":
#     """
#     Covert a quaternion into a full three-dimensional rotation matrix.
 
#     Input
#     :param Q: A 4 element array representing the quaternion (q0,q1,q2,q3) 
 
#     Output
#     :return: A 3x3 element matrix representing the full 3D rotation matrix. 
#              This rotation matrix converts a point in the local reference 
#              frame to a point in the global reference frame.
#     """
#     # Extract the values from Q
#     q0 = -0.000172323
#     q1 = 0.733736
#     q2 = -0.00010626
#     q3 = 0.679435



#     # First row of the rotation matrix
#     r00 = 2 * (q0 * q0 + q1 * q1) - 1
#     r01 = 2 * (q1 * q2 + q0 * q3)
#     r02 = 2 * (q1 * q3 - q0 * q2)
     
#     # Second row of the rotation matrix
#     r10 = 2 * (q1 * q2 - q0 * q3)
#     r11 = 2 * (q0 * q0 + q2 * q2) - 1
#     r12 = 2 * (q2 * q3 + q0 * q1)
     
#     # Third row of the rotation matrix
#     r20 = 2 * (q1 * q3 + q0 * q2)
#     r21 = 2 * (q2 * q3 - q0 * q1)
#     r22 = 2 * (q0 * q0 + q3 * q3) - 1
     

#     # 3x3 rotation matrix
#     rot_matrix = np.array([[r00, r01, r02],
#                            [r10, r11, r12],
#                            [r20, r21, r22]])
#     print(rot_matrix)


import numpy as np
import math
x=4.0
y=2.0
z=0.0
a1=a2=a3=a4=1.0
d3=((x**2+y**2)**0.5)-a3-a4
d1=z-a1-a2
T2=np.arctan2(y,x)

r0_6=[[-1.0,0.0,0.0],
      [0.0,-1.0,0.0],
      [0.0,0.0,1.0]]

r0_3=[[-np.sin(T2),0.0,np.cos(T2)],
      [np.cos(T2),0.0,np.sin(T2)],
      [0.0,1.0,0.0]]

inv_r0_3=np.linalg.inv(r0_3)

r3_6=np.dot(inv_r0_3,r0_6)

T5=np.arccos(r3_6[2][2])

T6=np.arccos(r3_6[2][0]/np.sin(T5))

T4=np.arccos(r3_6[1][2]/np.sin(T5))

print(T2)

print(T4)
print(T5)
print(T6)

