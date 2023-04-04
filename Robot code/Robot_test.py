from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
import numpy as np
#TEMP
array_ins=np.genfromtxt('generated_instructions0.csv', delimiter=',')


# Start the RoboDK API:
RDK = Robolink()

# Get the robot items by name:
robot = RDK.Item('UR5', ITEM_TYPE_ROBOT)

home= RDK.Item('Home')

Pick_base= RDK.Item('Pick_Base')
Place_base= RDK.Item('Place_Base')

World=RDK.Item('World',ITEM_TYPE_FRAME)
Ref_Pick=RDK.Item('Pick_Mat',ITEM_TYPE_FRAME)
Ref_Place=RDK.Item('Build_plate',ITEM_TYPE_FRAME)

#Functions:

def pick_place(frame,x,y,z,a,b,c,speed):
    robot.setFrame(frame)
    robot.setSpeed(speed)
    pose_ref=robot.Pose()
    Pick=Mat(pose_ref)

    pos_pick=Pick.Pos()
    pos_pick=[x,y,z]
    Pick.setPos(pos_pick)
    
    Pick=Pick*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)

    robot.MoveL(Pick)

    robot.setFrame(RDK.Item('UR5 Base'))


def movetype_place(frame,x,y,z,a,b,c,speed,mtype):
    robot.setFrame(frame)
    robot.setSpeed(speed)
    pose_ref=robot.Pose()
    Pick=Mat(pose_ref)

    #ending location
    pos_pick=Pick.Pos()
    pos_pick=[x,y,z+5]
    Pick.setPos(pos_pick)
    
    Pick=Pick*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)

    #movement type location
    #CHECK FOR CORRECT NOTATION
    Pick_move=Pick
    if mtype==1:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x,y,z+20]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)
    elif mtype==2:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x-5,y,z+20]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)
    elif mtype==3:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x,y+5,z+20]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)        
    elif mtype==4:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x-5,y+5,z+20]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)   


    robot.MoveL(Pick_move)
    robot.setSpeed(10)####MEMEBER
    robot.MoveL(Pick)

    robot.setFrame(RDK.Item('UR5 Base'))



t=0

speed_normal=100
speed_place=10
Tool_length=300 #THIS IS VERY HIGH

print('starting')
robot.setFrame(RDK.Item('UR5 Base'))
robot.MoveJ(home)

for x in range(0,2):


    robot.MoveJ(Pick_base)
    
    robot.MoveJ(Pick_base)

    #LXFML instructions
    robot.MoveJ(Place_base)
    


    robot.MoveJ(Place_base)

robot.setFrame(RDK.Item('UR5 Base'))
robot.MoveJ(home)
print('done')
