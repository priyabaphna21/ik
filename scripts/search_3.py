#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
import copy
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

#initilize moveit commander(to communicate with the move group)
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('pickplace', anonymous=True)
robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()
manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
grasping_group = moveit_commander.MoveGroupCommander("gripper")


group_variable_values = manipulator_group.get_current_joint_values()

# ground    
# group_variable_values[0] = 4.36332 #0.4887
# group_variable_values[1] = -1.65806 #-1.0123
# group_variable_values[2] = -1.55334 #2.1817
# group_variable_values[3] = -1.51844 #-2.7576
# group_variable_values[4] = -4.76475 #-1.5359
# group_variable_values[5] = -5.02655 #0.5236
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# left pan_top
# group_variable_values[0] = 0.31416
# group_variable_values[1] = -1.4137
# group_variable_values[2] = 1.53589
# group_variable_values[3] = -3.2114
# group_variable_values[4] = -1.309
# group_variable_values[5] = 0.03491
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)
# left pan_center
# group_variable_values[0] = 0.314159
# group_variable_values[1] = -1.25664
# group_variable_values[2] = 2.28638
# group_variable_values[3] = -4.13643
# group_variable_values[4] = -1.51844
# group_variable_values[5] = 1.64061
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)
   
# button_ 1 
# group_variable_values[0] = -0.10472
# group_variable_values[1] = -1.6057
# group_variable_values[2] = 1.98967
# group_variable_values[3] = -3.4732
# group_variable_values[4] = -1.44862
# group_variable_values[5] = 1.623156
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# button_2
# group_variable_values[0] = -0.57596
# group_variable_values[1] = -1.69297
# group_variable_values[2] = 2.09439
# group_variable_values[3] = -3.47321
# group_variable_values[4] = -0.97738
# group_variable_values[5] = 1.570796
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# button_3
# group_variable_values[0] = -0.92502
# group_variable_values[1] = -1.58825
# group_variable_values[2] = 2.02458
# group_variable_values[3] = -3.47321
# group_variable_values[4] = -0.62832
# group_variable_values[5] = 1.53589
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# button_4
# group_variable_values[0] = -0.92502 #-1.029744
# group_variable_values[1] = -0.82030 #-1.48353
# group_variable_values[2] = 2.09439 #2.44346
# group_variable_values[3] = -4.69494 #-4.01426
# group_variable_values[4] = -0.62832 #-0.610865
# group_variable_values[5] = 1.79769 #3.054323
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# button_5
# group_variable_values[0] = -0.57596 #-0.66323
# group_variable_values[1] =  -0.85521 #-1.22173
# group_variable_values[2] =  2.26893 #2.40855
# group_variable_values[3] =  -4.74729 #-4.24115
# group_variable_values[4] =  -0.95993 #-0.872664
# group_variable_values[5] =  1.69297 #1.55334
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# #button_6
# group_variable_values[0] = -0.12217 #-0.20944
# group_variable_values[1] = -0.83776 #-1.29154
# group_variable_values[2] = 2.19911 #2.3213
# group_variable_values[3] = -4.66003 #-4.11898
# group_variable_values[4] = -1.41372 #-1.32645
# group_variable_values[5] = 1.60570#0.03491
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# #button_7
# group_variable_values[0] = -2.33874 #-0.174533
# group_variable_values[1] = -2.18166 #-0.50615
# group_variable_values[2] = -2.26893 #2.26893
# group_variable_values[3] = 4.69494 #-4.85201
# group_variable_values[4] = -0.82030 #-1.36136
# group_variable_values[5] = -1.72788 #0.03491
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# #button_8
# group_variable_values[0] = -2.67035 #-0.55851
# group_variable_values[1] = -2.18166 #-0.610865
# group_variable_values[2] = -2.30383 #2.37365
# group_variable_values[3] = 4.66003 #-4.85201
# group_variable_values[4] = -1.13446 #-1.04719
# group_variable_values[5] = -1.65806 #-1.640609
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

#button_9
group_variable_values[0] = -3.10669 #-0.785398
group_variable_values[1] = -2.21657 #-0.593412
group_variable_values[2] = -2.14675 #2.303835
group_variable_values[3] = 4.53786 #-4.782202
group_variable_values[4] = -1.57079 #-0.8203047
group_variable_values[5] = -1.57079 #-3.211406
manipulator_group.set_joint_value_target(group_variable_values)

plan2 = manipulator_group.plan()
manipulator_group.go(wait=True)


# #window_cover
# group_variable_values[0] = -1.0996
# group_variable_values[1] = -1.7802
# group_variable_values[2] = 2.042
# group_variable_values[3] = -2.3387
# group_variable_values[4] = -1.1519
# group_variable_values[5] = 0.9774
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# #ground_right
# group_variable_values[0] = -1.4835
# group_variable_values[1] = -0.9948
# group_variable_values[2] = 2.0595
# group_variable_values[3] = -2.6878
# group_variable_values[4] = -1.5533
# group_variable_values[5] = 1.6406
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# #inspection_window
# group_variable_values[0] = -1.7453
# group_variable_values[1] = -1.4835
# group_variable_values[2] = 2.5831
# group_variable_values[3] = -2.042
# group_variable_values[4] = -0.1047
# group_variable_values[5] = 0.87266
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)

# #home
# group_variable_values[0] = 0
# group_variable_values[1] = -1.570796
# group_variable_values[2] = 0
# group_variable_values[3] = -1.570796
# group_variable_values[4] = 0
# group_variable_values[5] = 0
# manipulator_group.set_joint_value_target(group_variable_values)

# plan2 = manipulator_group.plan()
# manipulator_group.go(wait=True)


rospy.sleep(20)
moveit_commander.roscpp_shutdown()