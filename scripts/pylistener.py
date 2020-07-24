#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example Python node to listen on a specific topic."""

# Import required Python code.
import rospy
from std_msgs.msg import String

class PyListener(object):

    def __init__(self):
        """Configure subscriber."""
        # Create a subscriber with appropriate topic, custom message and name of
        # callback function.
        
        self.sub = rospy.Subscriber("chatter", String, self.callback)

        # Initialize message variables.
        self.enable = False
        self.data = ""

        if self.enable:
            self.start()
        else:
            self.stop()

    def start(self):
        self.enable = True
        self.sub = rospy.Subscriber("chatter", String, self.callback)

    def stop(self):
        """Turn off subscriber."""
        self.enable = False
        self.sub.unregister()

    def callback(self, data):
        """Handle subscriber data."""
        # Simply print out values in our custom message.
        self.data = data
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', self.data.data)

# Main function.
if __name__ == "__main__":
    # Initialize the node and name it.
    rospy.init_node("pyListener", anonymous=True)
    # Go to the main loop.
    listener = PyListener()
    listener.start()
    # Wait for messages on topic, go to callback function when new messages arrive.
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
