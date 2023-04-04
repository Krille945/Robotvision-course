from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
import numpy as np





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

def main_robot(runmode):
    #TEMP
    array_ins=np.genfromtxt('generated_instructions0.csv', delimiter=',')
    t=0

    speed_normal=100
    speed_place=10
    Tool_length=200 #CHECK BEFORE RUNNING

    print('starting')
    robot.setFrame(RDK.Item('UR5 Base'))
    robot.MoveJ(home)

    for x in range(20,len(array_ins[:,0])-1):


        robot.MoveJ(Pick_base)
        
        #camera func
        pick_place(Ref_Pick,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length+10,0,0,array_ins[x,3],speed_normal)
        pick_place(Ref_Pick,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length,0,0,0,speed_place)

        # activate IO

        robot.MoveJ(Pick_base)


        #LXFML instructions
        robot.MoveJ(Place_base)
        
        #Placing
        print('Placing:')
        print(array_ins[x,:])
        movetype_place(Ref_Place,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length,0,0,array_ins[x,3],speed_normal,array_ins[x,4])
        pick_place(Ref_Place,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length,0,0,0,speed_place)

        #Activate IO
        #Slow lift from place
        pick_place(Ref_Place,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length+10,0,0,0,speed_place)


        robot.MoveJ(Place_base)

    robot.setFrame(RDK.Item('UR5 Base'))
    robot.MoveJ(home)
    print('done')

if __name__ == '__main__':
    main_robot(1)