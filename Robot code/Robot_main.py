from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots

# Start the RoboDK API:
RDK = Robolink()

# Get the robot item by name:
robot = RDK.Item('UR5', ITEM_TYPE_ROBOT)

home= RDK.Item('Home')

target= RDK.Item('Target')
t=0
while True:
    robot.MoveJ(home)

    robot.MoveJ(target)
    t=t+1
    if t == 10:
        break
