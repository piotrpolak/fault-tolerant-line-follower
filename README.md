fault-tolerant-line-follower
============================

Khepera3 robot software.

Live demo: http://www.youtube.com/watch?v=raQ_id-nk2U

Robot description
-----------------
The robot follows continuous path, avoids simple obstacles and continues its way even if the path is broken (only on the straight sections). The robots stops after a certain period of time/distance of going out of the line (meaning the path has finished).

Khepera 3 robot is used.

I used Python along with PyBluez library. I wrote a mini-framework and abstracted each level of the application in such way that it can be easily parametrized - the software itself was written having no robot :) based on the command specification only. Then it came to tests, after some 30 min of trying to connect via bluethooth it finally worked!

Testing environment
-------------------
A black 3cm tape is used for the path, metal cans as obstacles and a table having a bright non-reflective surface is used.

Robot logic
-----------
At a certain moment the robot can be in one of the following states:

* initial state
* line follow state
* broken line state
* avoid obstacle state
* final state

Line follow state
-----------------

In this state the robot first check if there are no obstacles on his path (reads the front proximity sensors). If the obstacles are found, the robot jumps to the avoid obstacle state.

Otherwise the robot reads the values of the two ground proximity IR sensors in order to determine the color of the surface for both the left and the right sensors and adjusts the speed of the motors. The changes of the direction of the robot are smooth proportional to the readings of the above sensors.

If the readings of the both IR sensors say that the robot entered the "bright surface" the robot jumps to the broken line state.

Avoid obstacle state
--------------------

If there is an obstacle found on the path of the robot, the robot:

* changes its direction 90 degrees left
* goes perpendicular to the path until the moment it can turn right without touching the obstacle
* goes parallel to the path until the moment it can turn right without touching the obstacle
* jumps into the broken line state - this assures the robot continues its way even if the path is not straight or the turn angles are not exactly 90 degrees.

Broken line state
-----------------

In this state the robot continues going straight until it finds the path and it jumps into the line follow state.

If the path is not found in a certain period of time, the robot stops going and jumps into the final state.

Software description
--------------------

Robot software is written in Python in OOP manner. All the parameters are storied in a central Config.py file.

The robot logic is executed in a loop.

The software is run on a separate host (common desktop) and communicates with the Khepera 3 robot using raw commands over Bluetooth connection.

Software components
-------------------

* main.py - the main file that should be run
* Comm.py - the communication class responsible for connecting with the remote device via Bluetooth and sending/receiving raw commands
* Config.py - file containing all the configuration variables including the remote device's MAC and port
* Debugger.py - file containinig some debugging methods (print methods)
* Khepera.py - the Khepera API, uses Comm.py class
* RobotLogic.py - this class contains robot's logic, the main loop
* Software dependences
* PyBluez - Python Bluetooth bindings - https://pypi.org/project/PyBluez/
