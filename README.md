# beginner_tutorials

Extended version of the [ROS Tutorials](https://wiki.ros.org/ROS/Tutorials) for the [RobotCar](https://github.com/Michdo93/robotcar) to show the basic functionality of ROS and the RobotCar. 

## How to use

At first you have to run one roscore. Open a terminal window and execute `roscore`.

### Talker / Listener

The Talker and Listener uses the Publisher-Subscriber-Pattern of ROS. You can use it on one computer or across multiple machines. Further informations you can find inside the [ROS Tutorials](https://wiki.ros.org/ROS/Tutorials).

Open a terminal window and run `rosrun beginner_tutorials talker.py` to run the publisher.
For running the Subscriber you have to run `rosrun beginner_tutorials listener.py`.

### Two Ints

The Client-Server-Pattern of ROS can be used by an easy example. The client sends a request with two integer variables and the server answers with a response where it calculates the addition of this variables. You can use it on one computer or across multiple machines. Further informations you can find inside the [ROS Tutorials](https://wiki.ros.org/ROS/Tutorials).

To run the server you have to open a terminal and execute `rosrun beginner_tutorials add_two_ints_server.py`.
For the client you have to execute `rosrun beginner_tutorials add_two_ints_client.py`.


### Pytalker / Pylistener

The Pytalker and Pylistener are the same Talker and Listener the before. The only difference is that they are written object-oriented. This class model is used in all classes of the RobotCar. So it also uses the Publisher-Subscriber-Pattern of ROS. You can use it on one computer or across multiple machines. Further informations you can find inside the [ROS Tutorials](https://wiki.ros.org/ROS/Tutorials).

Open a terminal window and run `rosrun beginner_tutorials pytalker.py` to run the publisher.
For running the Subscriber you have to run `rosrun beginner_tutorials pylistener.py`.

### PyechoerTalker / PyechoerListener

The PyechoerTalker and PyechoerLister are object-oriented. The PyechoerTalker publishes an integer value and the PyechoerListener returns it to the PyechoerTalker. There the integer value gets incremented. It simulates changing values like as example a motor. It proofs that with this concept you can change values during runtime. The PyechoerLister could be an ADAS in this example. So it also uses the Publisher-Subscriber-Pattern of ROS. You can use it on one computer or across multiple machines. Further informations you can find inside the [ROS Tutorials](https://wiki.ros.org/ROS/Tutorials).

Open a terminal window and run `rosrun beginner_tutorials pyechoer_talker.py` to run the publisher.
For running the Subscriber you have to run `rosrun beginner_tutorials pyechoer_listener.py`.

### Pyechoer

The Pyechoer does exactly the same as the PyechoerTalker and PyechoerLister. The only difference is that it was written in one class. It proofs the concept of as example a motor node.

Open a terminal window and run `rosrun beginner_tutorials pyechoer.py` to run the publisher and subscriber inside one class.
