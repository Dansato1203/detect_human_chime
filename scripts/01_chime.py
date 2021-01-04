#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rosnode
from playsound import playsound
from std_msgs.msg import Int32

def callback(data):
  print('お客様が{0}名でご来店されました。'.format(data.data))
  playsound("konnbini.mp3")


def main():
  rospy.init_node("chime_no1_node")

  print("お客様がご来店されたら入店音を鳴らします。")
  
  sub = rospy.Subscriber("/detect_face", Int32, callback)
  rospy.spin()


if __name__ == '__main__':

    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
