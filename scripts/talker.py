#!/usr/bin/env python
import os
import sys
import cv2
import edgetpu
import getpass
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "time: %s and python%s and opencv-python: %s and edgetpu: %s" % (rospy.get_time(), sys.version_info[0], cv2.__version__, edgetpu.__version__)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

        if pub.get_num_connections() >= 1:
            pub.publish(hello_str)
            raise rospy.ROSInterruptException

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
