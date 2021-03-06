#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
  def __init__(self):
     self.image_pub = rospy.Publisher("image_topic", Image, queue_size=1)
     self.bridge = CvBridge()
     self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
     
  def callback(self,data):
     pub1 = rospy.Publisher("detect_face", Int32, queue_size=1)
     pub2 = rospy.Publisher("number_of_face", Int32, queue_size=1)
     try:
       cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
     except CvBridgeError as e:
       print(e)


     #分類器までのパス
     faceCascade = cv2.CascadeClassifier('/home/dan/catkin_ws/src/detect_human_chime/scripts/haarcascade_frontalface_alt2.xml')

     #グレースケール
     gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

     #顔判定
     face = faceCascade.detectMultiScale(gray,1.1,3,minSize=(50,50))

     #フラッグ 顔があれば1, なければ0をパブリッシュする
     flag = 1

     #顔周りに四角
     if len(face) > 0:
       for rect in face:
         cv2.rectangle(cv_image, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (255, 255, 255), thickness=2)
       print("face")
       print('{0}人ご来店'.format(len(face)))
       pub2.publish(len(face))
     else:
       flag = 0
     
     pub1.publish(flag)

     cv2.imshow('detected_face', cv_image)
     cv2.waitKey(3)

def main(args):
  rospy.init_node('image_converter', anonymous=True)
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
    rospy.spin()
