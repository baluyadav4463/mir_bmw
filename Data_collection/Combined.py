#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import rostopic
from rostopic import  ROSTopicHz
import time

class Server:
    def __init__(self):
        self.lidar = None
        self.camera = None
        self.lidar_pre=0
        self.i=1
        

    def lidar_callback(self, msg):
        self.lidar = msg
        self.lidar_pre=self.lidar.data
        print('Lidar:- ' )
        print(self.lidar)        

        

    def camera_callback(self, msg):
        self.camera = msg
        print('Camera:- ')
        print(self.camera)
        self.prediction()
        

    
    def prediction(self):
        global Prediction
        if self.lidar==None :
                if(self.i>2):
                    self.i=1
                print(self.i)
                fact=(1-(self.i/10.0))
                Prediction=((self.camera.data)+(self.lidar_pre*fact))
                self.i=self.i+1
        else :
            Prediction=(self.lidar.data)
            self.lidar=None
        print('prediction')
        print(Prediction)

class edit(ROSTopicHz):
    def goas(self):
        time=ROSTopicHz(-1)
        time.print_hz()
        print(time.rate)




def getting_rates():

    r = rostopic.ROSTopicHz(-1)
    s = rospy.Subscriber('/Lidar_Prediction', Float32, r.callback_hz, callback_args='/Lidar_Prediction')
    l = rospy.Subscriber('/Camera_Prediction', Float32, r.callback_hz, callback_args='/Camera_Prediction')
    rospy.sleep(1)
    r.print_hz(['/Lidar_Prediction'])
    r.print_hz(['/Camera_Prediction'])




if __name__ == '__main__':
    rospy.init_node('combined')
    getting_rates()
    rospy.sleep(5)
    server = Server()
    rospy.Subscriber('/Lidar_Prediction', Float32 , server.lidar_callback)
    rospy.Subscriber('/Camera_Prediction', Float32, server.camera_callback)
    while not rospy.is_shutdown():
        try:
            
            rospy.spin()

 	except KeyboardInterrupt:
             break
             
