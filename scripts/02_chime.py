#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rosnode
import message_filters
from playsound import playsound
from std_msgs.msg import Int32

def callback(msg1, msg2):
  det_face = msg1.data
  if det_face == 1:
    print('お客様が{0}名でご来店されました。'.format(msg2.data))
    playsound("/home/dan/catkin_ws/src/detect_human_chime/scripts/konnbini_2.mp3")
    rospy.sleep(5)

def main():
  rospy.init_node("chime_no2_node")

  print("お客様がご来店されたら入店音を鳴らします。")
  
  sub1 = message_filters.Subscriber('detect_face', Int32)
  sub2 = message_filters.Subscriber('number_of_face', Int32)

  queue_size = 1
  fps = 100.
  delay = 1 / fps * 0.5

  mf = message_filters.ApproximateTimeSynchronizer([sub1, sub2], queue_size, delay, allow_headerless=True)
  mf.registerCallback(callback)

  rospy.spin()


if __name__ == '__main__':

    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
