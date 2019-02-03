#!/usr/bin/env python

import datetime
import os
import cv2
import time
import rospy
import sys
import numpy as np
from sensor_msgs.msg import Joy
from threading import Thread
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from image_converter import ImageConverter
from drive_run import DriveRun
from config import Config
from image_process import ImageProcess
xMin = 0
yMin = 0
xMax = 640
yMax = 310
class lidar:
    def __init__(self):
        rospy.init_node('BMW_controller_lidar')
     	self.rate = rospy.Rate(20)
        self.ic = ImageConverter()
        self.image_process = ImageProcess()
        self.drive= DriveRun(sys.argv[1])
        rospy.Subscriber('/image_topic_2', Image, self.controller_cb)
        self.image = None
        self.lidar_processed = False

    def controller_cb(self, image): 
        img = self.ic.imgmsg_to_opencv(image)
        img = cv2.resize(img,(160,70))
        self.image = self.image_process.process(img)
        self.lidar_processed = True

class camera:
    def __init__(self):
        self.ic = ImageConverter()
        self.image_process = ImageProcess()
        self.driveC= DriveRun(sys.argv[2])
        rospy.Subscriber('/usb_cam/image_raw', Image, self.recorder1)
        self.imageC = None
        self.camera_processed = False

    def recorder1(self, image):
	cam_img = self.ic.imgmsg_to_opencv(image)
	cropImg = cam_img[yMin:yMax,xMin:xMax]
        self.imageC = cv2.resize(cropImg,(160,70))
        self.camera_processed = True

if __name__ == "__main__":
    try:

        neural_control_lidar= lidar()
	neural_control_camera= camera()
        while not rospy.is_shutdown():
            if neural_control_camera.camera_processed == True and neural_control_lidar.lidar_processed==True :
                predictionL = neural_control_lidar.drive.run(neural_control_lidar.image)
		print("lidar")
                print(predictionL)
    		predictionC= neural_control_camera.driveC.run(neural_control_camera.imageC)
		print("Camera")
                print(predictionC)
		prediction=predictionC+predictionL
                #neural_control.pub.publish(prediction)
		print(prediction)
		joy_pub = rospy.Publisher('/joy', Joy, queue_size = 10)
	        rate = rospy.Rate(30)
      	  	joy_data = Joy()
#####################################################################################    
        	if(prediction[0][0] < 0.1 and prediction[0][0] > -0.1):
            		print("straight")
            		prediction[0][0] = prediction[0][0]
            		joy_data.axes = [0,0,0,0,0,0]
            		joy_data.buttons = [0,0,0,1,0,0,0,1,0,0,0,0]
#####################################################################################
        	elif(prediction[0][0] < 0.5 and prediction[0][0] > 0.1):
            		print("Left")
            		prediction[0][0] = prediction[0][0]
            		joy_data.axes = [0,0,0,0,1.0,0]
            		joy_data.buttons = [0,0,0,0,0,0,0,1,0,0,0,0]
#####################################################################################
        	elif(prediction[0][0] < 1 and prediction[0][0] > 0.5):
            		print("Ext.Left")
            		prediction[0][0] = prediction[0][0]
            		joy_data.axes = [0,0,0,0,0,1.0]
            		joy_data.buttons = [0,0,0,0,0,0,0,1,0,0,0,0]
#####################################################################################        
        	elif(prediction[0][0] < -0.1 and prediction[0][0] > -0.5):
            		print("Right")
            		prediction[0][0] = -prediction[0][0]
            		joy_data.axes = [0,0,0,0,-1.0,0]
            		joy_data.buttons = [0,0,0,0,0,0,0,1,0,0,0,0]
#####################################################################################
        	elif(prediction[0][0] < -0.5 and prediction[0][0] > -1):
            		print("Ext.Right")
            		prediction[0][0] = prediction[0][0]
            		joy_data.axes = [0,0,0,0,0,-1.0]
            		joy_data.buttons = [0,0,0,0,0,0,0,1,0,0,0,0]
#####################################################################################
        	joy_pub.publish(joy_data)

                neural_control_camera.camera_processed = False
		neural_control_lidar.lidar_processed=False
 		neural_control_lidar.rate.sleep()

    except KeyboardInterrupt:
          print ('\nShutdown requested. Exiting...')
    
