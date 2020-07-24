#!/usr/bin/env python
import os
import sys
import cv2
import edgetpu
import rospy
from std_msgs.msg import String

env=os.path.expanduser(os.path.expandvars('/home/ros'))
sys.path.insert(0, env)

from Adafruit_Python_PCA9685 import Adafruit_PCA9685


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
