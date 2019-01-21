#!/usr/bin/env python

from cv_bridge import CvBridge, CvBridgeError

class ImageConverter:
    def __init__(self):
        #load CvBridge for conversion to and from ros image messages
        self.bridge = CvBridge()

    def opencv_to_imgmsg(self, cv_img):
        try:
            img_msg = self.bridge.cv2_to_imgmsg(cv_img, 'bgr8')
            return img_msg
        except CvBridgeError as err:
            return err

    def imgmsg_to_opencv(self, img_msg):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(img_msg, 'bgr8')
            return cv_img
        except CvBridgeError as err:
            return err
