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

def tocontinue():
    while True:
        input_var=input("If pickup/place is correct press \"y\": ")
        if input_var =="y":
            print("\n")

        else:
            print("You have to choose yes or no by typing \"y\" or \"n\" \n")
        
        break

def runmode():
    while True:
        input_var=input("To run LIVE press \"y\" or to run OFFLINE press \"n\": ")
        if input_var =="y":
            print("\n")
            print("ONLINE")
            return 1
        elif input_var=="n":
            print("\n")
            print("OFFLINE")
            return 0

        else:
            print("You have to choose yes or no by typing \"y\" or \"n\" \n")
        
        break

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
    if runmode==1:
        # Update connection parameters if required:
        robot.setConnectionParams('192.168.10.101',30000,'/', 'anonymous','')

        # Connect to the robot using default IP
        success = robot.Connect()  # Try to connect once
        #success robot.ConnectSafe() # Try to connect multiple times
        status, status_msg = robot.ConnectedState()
        if status != ROBOTCOM_READY:
            # Stop if the connection did not succeed
            print(status_msg)
            raise Exception("Failed to connect: " + status_msg)

        # This will set to run the API programs on the robot and the simulator (online programming)
        RDK.setRunMode(RUNMODE_RUN_ROBOT)
        # Note: This is set automatically when we Connect() to the robot through the API


        joints_ref = robot.Joints()
        tocontinue()    
    else:
        RDK.setRunMode(RUNMODE_SIMULATE)    
    t=0

    speed_normal=100
    speed_place=10
    Tool_length=300 #THIS IS VERY HIGH

    print('starting')
    robot.setFrame(RDK.Item('UR5 Base'))
    robot.setSpeed(speed_place)
    robot.MoveL(home)
    tocontinue()
    for x in range(0,2):


        robot.MoveL(Pick_base)
        tocontinue()

        #LXFML instructions
        robot.MoveL(Place_base)
        tocontinue()
        


    robot.setFrame(RDK.Item('UR5 Base'))
    robot.MoveL(home)
    print('done')


if __name__ == '__main__':
    mode=runmode()
    main_robot(mode)#THIS WILL RUN LIVE