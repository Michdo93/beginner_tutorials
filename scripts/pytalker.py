#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import required Python code.
import os
import sys
import cv2
import edgetpu
import getpass
import rospy
from std_msgs.msg import String

env=os.path.expanduser(os.path.expandvars('/home/' + getpass.getuser()))
sys.path.insert(0, env)

from Adafruit_Python_PCA9685 import Adafruit_PCA9685


class PyTalker(object):
    """Node example class."""

    def __init__(self):
        self.pub = rospy.Publisher("chatter", String, queue_size=10)
        self.rate = rospy.Rate(10) # 10hz

        # Initialize message variables.
        self.enable = False
        self.message = ""

        if self.enable:
            self.start()
        else:
            self.stop()

    def start(self):
        """Turn on publisher."""
        self.enable = True
        self.pub = rospy.Publisher("chatter", String, queue_size=10)

        while not rospy.is_shutdown():
            self.message = "time: %s and python%s and opencv-python: %s and edgetpu: %s" % (rospy.get_time(), sys.version_info[0], cv2.__version__, edgetpu.__version__)
            rospy.loginfo(self.message)
            self.pub.publish(self.message)
            self.rate.sleep()

    def stop(self):
        """Turn off publisher."""
        self.enable = False
        self.pub.unregister()

# Main function.
if __name__ == "__main__":
    # Initialize the node and name it.
    rospy.init_node("pyTalker", anonymous=True)
    # Go to class functions that do all the heavy lifting.

    talker = PyTalker()

    try:
        talker.start()
    except rospy.ROSInterruptException:
        pass
    # Allow ROS to go to all callbacks.
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
