#! /usr/bin/env python

import rospy
import sys
import numpy as np
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from gazebo_msgs.srv import GetModelState
from fiducial_msgs.msg import FiducialTransformArray
from geometry_msgs.msg import Transform



global sub

class tag_info():
    aruco_id = None 
    position_x = None 
    position_y = None 
    position_z = None 

list = []

list.append(tag_info())
list.append(tag_info())
list.append(tag_info())
list.append(tag_info())
list.append(tag_info())
list.append(tag_info())

def main():

    manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
    group_variable_values = manipulator_group.get_current_joint_values()
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()     

    group_variable_values[0] = 0.4887
    group_variable_values[1] = -1.0123
    group_variable_values[2] = 2.1817
    group_variable_values[3] = -2.7576
    group_variable_values[4] = -1.5359
    group_variable_values[5] = 0.5236
    manipulator_group.set_joint_value_target(group_variable_values)

    plan2 = manipulator_group.plan()
    manipulator_group.go(wait=True)

    sub = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    matrix = transformation(sub)
    A_id = save_id(sub)

    waypoint_1 = np.array([[ 0.03398006,  0.99022806, -0.13524068, 0.21311],
                                [ 0.99939653,  -0.03461061, -0.00228688, 0.3294],
                                [-0.00694507, -0.13508159,  -0.99081012, 0.087242 ],
                                [ 0, 0, 0, 1]])

    aruco = np.matmul(waypoint_1, matrix)

    list[0].aruco_id = A_id
    list[0].position_x = aruco[0,3]
    list[0].position_y = aruco[1,3]
    list[0].position_z = aruco[2,3]

    print (list[0].aruco_id)
    print (list[0].position_x, list[0].position_y, list[0].position_z)

    group_variable_values[0] = 0.314159
    group_variable_values[1] = -1.25664
    group_variable_values[2] = 2.28638
    group_variable_values[3] = -4.13643
    group_variable_values[4] = -1.51844
    group_variable_values[5] = 1.64061
    manipulator_group.set_joint_value_target(group_variable_values)

    plan2 = manipulator_group.plan()
    manipulator_group.go(wait=True)

    sub = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    matrix = transformation(sub)
    A_id = save_id(sub)

    waypoint_2 = np.array([[ 0.2195349,   0.00850069,  0.9755662, 0.2239 ],
                            [ 0.35524536,  -0.93200981,  -0.07182131, 0.18888],
                            [ 0.90862666,  0.36233314, -0.20763068, 0.37044],
                            [0, 0, 0, 1]])

    aruco = np.matmul(waypoint_2, matrix)

    list[1].aruco_id = A_id
    list[1].position_x = aruco[0,3]
    list[1].position_y = aruco[1,3]
    list[1].position_z = aruco[2,3]
    
    print (list[1].aruco_id)
    print (list[1].position_x, list[1].position_y, list[1].position_z)


    rospy.spin()
    moveit_commander.roscpp_shutdown()

def save_id(msg):
    for m in msg.transforms:
        tag_id = m.fiducial_id
    
    return tag_id

def transformation(msg):
    for m in msg.transforms:
        trans = m.transform.translation
        rot = m.transform.rotation
        t = Transform()

        t.translation.x = trans.x
        t.translation.y = trans.y
        t.translation.z = trans.z
        t.rotation.x = rot.x
        t.rotation.y = rot.y
        t.rotation.z = rot.z
        t.rotation.w = rot.w

        q0 = t.rotation.w
        q1 = t.rotation.x 
        q2 = t.rotation.y
        q3 = t.rotation.z

        # First row of the rotation matrix
        r00 = 2 * (q0 * q0 + q1 * q1) - 1
        r01 = 2 * (q1 * q2 + q0 * q3)
        r02 = 2 * (q1 * q3 - q0 * q2)
        
        # Second row of the rotation matrix
        r10 = 2 * (q1 * q2 - q0 * q3)
        r11 = 2 * (q0 * q0 + q2 * q2) - 1
        r12 = 2 * (q2 * q3 + q0 * q1)
        
        # Third row of the rotation matrix
        r20 = 2 * (q1 * q3 + q0 * q2)
        r21 = 2 * (q2 * q3 - q0 * q1)
        r22 = 2 * (q0 * q0 + q3 * q3) - 1

        trans_matrix = np.array([[r00, r01, r02, t.translation.x],
                        [r10, r11, r12, t.translation.y],
                        [r20, r21, r22, t.translation.z],
                        [0, 0, 0, 1]])

        return trans_matrix

if __name__ == "__main__":
    rospy.init_node('maintenance', anonymous=True)
    main()