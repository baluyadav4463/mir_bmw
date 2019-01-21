#!/usr/bin/env python

import rospy
import cv2
import os
import rospy
import datetime
import time
import numpy as np
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image
from image_converter import ImageConverter
from std_msgs.msg import String
xMin = 0
yMin = 0
xMax = 640
yMax = 310
vehicle_steer = 0

ic = ImageConverter()
path = '/home/yadav/New_Data_collection/' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '/')
if os.path.exists(path + 'stacked_only'):
    print('path exists. continuing...')
else:
    os.makedirs(path + 'stacked_only')


stacked_only_text = open(str(path) + 'stacked_only/' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt", "w+")

def callback(value):
    global vehicle_steer
    #vehicle_vel = value.linear.x
    vehicle_steer = value.y
    
def recorder1(data): 
    img1 = ic.imgmsg_to_opencv(data)
    global time_stamp
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    cropImg = img1[yMin:yMax,xMin:xMax]
    global newimg
    newimg = cv2.resize(cropImg,(160,50))
    # 	time.sleep(0.166666667)
    
    
    

def recorder2(data):
    img = ic.imgmsg_to_opencv(data)
    img_resize = cv2.resize(img,(160,50))
    stacked_img = np.concatenate((img_resize,newimg), axis=0)
    cv2.imwrite(str(path) + 'stacked_only/' + str(time_stamp) + '.jpg',stacked_img)
    stacked_only_text.write(str(time_stamp) + ',' + str(vehicle_steer) + "\r\n")

    
def main():
   rospy.init_node('data_collection_stacked')
   rospy.Subscriber("/pos", Vector3, callback)
   rospy.Subscriber('/usb_cam/image_raw', Image, recorder1)
   rospy.Subscriber('/image_topic_2', Image, recorder2)
   rospy.spin()

if __name__ == '__main__':
    main()
