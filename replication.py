#!/usr/bin/env python3

import rospy
import vectors
from numpy import pi
from replicare.msg import CoordsArray
from std_msgs.msg import Float64

def do_the_math(data):
    #getting coords from topic: "pose_coords"
    right_wrist     = data.coords[0]
    right_elbow     = data.coords[1]
    right_shoulder  = data.coords[2]
    neck            = data.coords[3]
    left_shoulder   = data.coords[4]
    left_elbow      = data.coords[5]
    left_wrist      = data.coords[6]

    #calculating the angles
    right_shoulder_roll_angle = pi - vectors.calculate_angle(right_elbow, right_shoulder, neck)
    if right_elbow.y < right_shoulder.y:
        right_shoulder_roll_angle = -1 * right_shoulder_roll_angle

    right_elbow_angle = pi - vectors.calculate_angle(right_wrist, right_elbow, right_shoulder)
    if right_wrist.y < right_elbow.y:
        right_elbow_angle = -1 * right_elbow_angle

    left_shoulder_roll_angle = pi - vectors.calculate_angle(left_elbow, left_shoulder, neck)
    if left_elbow.y > left_shoulder.y:
        left_shoulder_roll_angle = -1 * left_shoulder_roll_angle

    left_elbow_angle = pi - vectors.calculate_angle(left_wrist, left_elbow, left_shoulder)
    if left_wrist.y > left_elbow.y:
        left_elbow_angle = -1 * left_elbow_angle

    #publishing to simulation
    rospy.Publisher('/RepliCare/right_shoulder_roll_position_controller/command', Float64, queue_size = 10).publish(right_shoulder_roll_angle)
    rospy.Publisher('/RepliCare/right_elbow_position_controller/command', Float64, queue_size = 10).publish(right_elbow_angle)
    rospy.Publisher('/RepliCare/left_shoulder_roll_position_controller/command', Float64, queue_size = 10).publish(left_shoulder_roll_angle)
    rospy.Publisher('/RepliCare/left_elbow_position_controller/command', Float64, queue_size = 10).publish(left_elbow_angle)

def listener():
    rospy.init_node('math')
    rospy.Subscriber('pose_coords', CoordsArray, do_the_math)
    rospy.spin()

def main():
    listener()

if __name__ == '__main__':
    main()
