#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import required Python code.
import os
import sys
import rospy
from std_msgs.msg import Int64

class PyEchoer(object):
    """Node example class."""

    def __init__(self):
        # Start with value 0.
        self.value = 0

        # Initialize message variables.
        self.enable = False
        self.message = ""   # message to send
        self.data = ""      # message received

        # if not looping.
        self.pub = rospy.Publisher("echo/set", Int64, queue_size=10)
        self.sub = rospy.Subscriber("echo/get", Int64, self.callback)

        self.rate = rospy.Rate(10) # 10hz

        if self.enable:
            self.start()
        else:
            self.stop()

    def start(self):
        """Turn on publisher and subscriber."""
        self.enable = True
        self.pub = rospy.Publisher("echo/set", Int64, queue_size=10)
        self.sub = rospy.Subscriber("echo/get", Int64, self.callback)

        while not rospy.is_shutdown():
            self.message = self.value + 1
            rospy.loginfo('I send %s', self.message)
            self.pub.publish(self.message)
            self.rate.sleep()

    def stop(self):
        """Turn off publisher and subscriber."""
        self.enable = False
        self.pub.unregister()
        self.sub.unregister()

    def callback(self, data):
        """Handle subscriber data."""
        self.data = data
        self.value = self.data.data
        rospy.loginfo(rospy.get_caller_id() + ' I heard %s', self.data.data)

# Main function.
if __name__ == "__main__":
    # Initialize the node and name it.
    rospy.init_node("pyListener", anonymous=True)
    # Go to class functions that do all the heavy lifting.

    echo = PyEchoer()

    try:
        echo.start()
    except rospy.ROSInterruptException:
        pass
    # Allow ROS to go to all callbacks.
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
