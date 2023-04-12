from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
import numpy as np
import cv2

import MV
import RVTransform



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
        pos_pick=[x-1,y+1,z+11]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)
    elif mtype==2:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x-5,y+1,z+11]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)
    elif mtype==3:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x-1,y+5,z+11]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)        
    elif mtype==4:
        pose_ref=robot.Pose()
        Pick_move=Mat(pose_ref)

        #ending location
        pos_pick=Pick.Pos()
        pos_pick=[x-5,y+5,z+11]
        Pick_move.setPos(pos_pick)
        Pick_move=Pick_move*rotx(a*pi/180)*roty(b*pi/180)*rotz(c*pi/180)   


    robot.MoveL(Pick_move)
    robot.setSpeed(10)####MEMEBER
    tocontinue()
    robot.MoveL(Pick)

    robot.setFrame(RDK.Item('UR5 Base'))

def open():
    #open
    robot.setDO(0,0) 
    robot.setDO(1,1) 

def close():
    #Close
    robot.setDO(0,1) 
    robot.setDO(1,0) 

def main_robot(runmode):

    #webcam = cv2.VideoCapture(1)

    if runmode==1:
        # Update connection parameters if required:
        # robot.setConnectionParams('192.168.2.35',30000,'/', 'anonymous','')

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
        print("Ready to start")
        tocontinue()    
    else:
        RDK.setRunMode(RUNMODE_SIMULATE)
    #TEMP
    array_ins=np.genfromtxt('generated_instructions0.csv', delimiter=',')
    t=0



    speed_normal=50
    speed_place=10
    Tool_length=147.5 #CHECK BEFORE RUNNING ### but run with the safety first

    print('starting')
    robot.setFrame(RDK.Item('UR5 Base'))
    robot.setSpeed(50)
    open()
    robot.MoveL(home)

    for x in range(0,len(array_ins[:,0])-1): ########CHECK
        px_to_mm_x=1.54
        px_to_mm_y=1.5
        xcam,ycam,Ccam=MV.get_xyA(array_ins[x,6],array_ins[x,7])
        xcam=xcam/px_to_mm_x #####MEMBER
        ycam=ycam/px_to_mm_y #####MEMBER
        Coords,Angle=RVTransform.Transform(xcam,ycam,Ccam)

        print('\nThe Results are then:')
        print('Cords:'+str(Coords))
        print('Angle:'+str(Angle))
        
        robot.MoveL(Pick_base)
        

        pick_place(Ref_Pick,ycam,xcam,12.8+Tool_length+10,0,0,-90+Ccam,speed_normal)
        tocontinue()
        pick_place(Ref_Pick,ycam,xcam,12.8+Tool_length,0,0,0,speed_place)

        close()
        robot.setSpeed(50)
        robot.MoveL(Pick_base)


        #LXFML instructions
        robot.MoveL(Place_base)
        
        #Placing
        print('Placing:')
        print(array_ins[x,:])
        #execute the movement type from 20 mm above to 5 mm
        movetype_place(Ref_Place,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length+11,0,0,-90+array_ins[x,3],speed_normal,array_ins[x,4])
        #placeing straight down
        pick_place(Ref_Place,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length+11.8,0,0,0,speed_place)

        #Activate IO
        open()

        
        #Slow lift from place
        pick_place(Ref_Place,array_ins[x,0],array_ins[x,1],array_ins[x,2]+Tool_length+15,0,0,0,speed_place)
        robot.setSpeed(50)

        robot.MoveL(Place_base)

    robot.setFrame(RDK.Item('UR5 Base'))
    robot.setSpeed(50)
    robot.MoveL(home)
    print('done')

if __name__ == '__main__':
    mode=runmode()
    main_robot(mode)#THIS CAN RUN LIVE
    