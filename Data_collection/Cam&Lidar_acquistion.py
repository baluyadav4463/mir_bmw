#!/usr/bin/env python

import rospy
import cv2
import os
import rospy
import datetime
import time
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image
from image_converter import ImageConverter
from std_msgs.msg import String

vehicle_steer = 0
#vehicle_vel = 0
xMin = 0
yMin = 0
xMax = 640
yMax = 310


ic = ImageConverter()
path = '/home/yadav/New_Data_collection/' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '/')
if os.path.exists(path + 'camera_only'):
    print('path exists. continuing...')
else:
    os.makedirs(path + 'camera_only')

if os.path.exists(path + 'lidar_only'):
    print('path exists. continuing...')
else:
    os.makedirs(path + 'lidar_only')

camera_text = open(str(path) + 'camera_only/' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt", "w+")

lidar_text = open(str(path) + 'lidar_only/' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt", "w+")

def callback(value):
    global vehicle_steer
    #vehicle_vel = value.linear.x
    vehicle_steer = value.y
    
def recorder1(data):
    img = ic.imgmsg_to_opencv(data)
    cropImg = img[yMin:yMax,xMin:xMax]
    newimg = cv2.resize(cropImg,(160,70))
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    cv2.imwrite(str(path) + 'camera_only/' + str(time_stamp) + '.jpg',newimg)
    camera_text.write(str(time_stamp) + ',' + str(vehicle_steer) + "\r\n")

def recorder2(data):
    img = ic.imgmsg_to_opencv(data)
    newimg = cv2.resize(img,(160,70))
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    cv2.imwrite(str(path) + 'lidar_only/' + str(time_stamp) + '.jpg',newimg)
    lidar_text.write(str(time_stamp) + ',' + str(vehicle_steer) + "\r\n")


def main():
   rospy.init_node('data_collection')
   rospy.Subscriber("/pos", Vector3, callback)
   rospy.Subscriber('/usb_cam/image_raw', Image, recorder1)
   rospy.Subscriber('/image_topic_2', Image, recorder2)
   rospy.spin()

if __name__ == '__main__':
    main()
