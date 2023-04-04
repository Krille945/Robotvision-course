from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots

# Start the RoboDK API:
RDK = Robolink()

# Get the robot item by name:
robot = RDK.Item('UR5', ITEM_TYPE_ROBOT)

home= RDK.Item('Home')

Pick_base= RDK.Item('Pick_Base')
Place_base= RDK.Item('Place_Base')
t=0
while True:
    robot.MoveJ(home)

    robot.MoveJ(Pick_base)
    robot.MoveJ(Place_base)
    t=t+1
    if t == 100:
        break
