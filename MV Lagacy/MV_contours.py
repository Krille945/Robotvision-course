import cv2
import numpy as np
import Mv_math

def get_xyA(type,colour):
    avg_center_list_x=[]
    avg_center_list_y=[]
    list_of_x=[]
    list_of_y=[]
    list_of_angle=[]
    list_of_type=[]
    Found=False
    p1x=[]
    p2x=[]
    p3x=[]
    p1y=[]
    p2y=[]
    p3y=[]
    print('Package Imported')

    webcam = cv2.VideoCapture(1)
    webcam.set(700,900) #width of webcam
    webcam.set(700,900) # height
    '''
    if colour == 0: 
        lower = np.array([0,0,180])
        upper = np.array([179,27,255])
    elif colour == 1:
        lower = np.array([0,40,180])
        upper = np.array([179,255,255])
    elif colour == 2:
        lower = np.array([0,105,164])
        upper = np.array([179,255,255])
    elif colour == 3:
        lower = np.array([97,0,176])
        upper = np.array([127,255,255])
    '''
    if colour == 0: #white
        lower = np.array([0,0,180])
        upper = np.array([179,27,255])
    elif colour == 1: #yellow
        lower = np.array([0,40,180])
        upper = np.array([179,255,255])
    elif colour == 2: #grey
        lower = np.array([0,0,140])
        upper = np.array([179,26,169])
    elif colour == 3: #red
        lower = np.array([0,0,180])
        upper = np.array([179,255,255])  
    t=0
    while True:

        succes, img = webcam.read() #define a variable called img, which is my webcam # success is a boolen which tells if we captured the video
        #img = img[98:310,405:638]

        #CONVERT TO HSV
        imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV,lower,upper)

        #create image result based on mask
        img = cv2.bitwise_and(img,img,mask=mask)

        cannyImg = cv2.Canny(img,20,200)

        contours,hierarchy = cv2.findContours(cannyImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            New_brick=True
            area = cv2.contourArea(cnt)

            if  area > 200: #needs calibrating
                arcLength = cv2.arcLength(cnt,True)
                corners = cv2.approxPolyDP(cnt, 0.04*arcLength,True) 
                nbCorners = len(corners)

                if nbCorners == 4:
                    center=np.zeros(2)
                    Cor=np.zeros((4,2))
                    cv2.drawContours(img, cnt, -1, (0, 255, 0),2)

                    brick_type = 1                   
                    #print('LEGO is found')

                    Cor[0,:] = np.fromstring(corners[0], dtype=int,sep='')
                    Cor[1,:] = np.fromstring(corners[1], dtype=int,sep='')
                    Cor[2,:] = np.fromstring(corners[2], dtype=int,sep='')
                    Cor[3,:] = np.fromstring(corners[3], dtype=int,sep='')
                    print(Cor)
                    center[0]=np.mean((Cor[:,0]))
                    center[1]=np.mean((Cor[:,1]))
                    points=np.array(Cor)
                    print(Cor)
                    ind = np.lexsort((points[:,1],points[:,0]))
                    Cor=Cor[ind]
                    for i in range(0, 4):
                        cv2.circle(img, (int(Cor[i,0]), int(Cor[i,1])), 2, (0, 0, 255), 2)

                    cv2.circle(img, (int(center[0]), int(center[1])), 2, (255, 0, 0), 2)

                    Brick_type=Mv_math.Type_finder(Cor[0,:],Cor[1,:],Cor[3,:])####

                    #print(Brick_type)
                    
                    #### SAVE in brick or create new 
                    for i in range(0,len(avg_center_list_x[:])):

                        if center[0]+20 > avg_center_list_x[i] >center[0]-20 and center[1]+20 > avg_center_list_y[i] >center[1]-20:
                            brick_index=i
                            New_brick=False
                            



                            p1x[i].append(Cor[0,0])
                            p2x[i].append(Cor[1,0])
                            p3x[i].append(Cor[3,0])
                            p1y[i].append(Cor[0,1])
                            p2y[i].append(Cor[1,1])
                            p3y[i].append(Cor[3,1])



    

                            list_of_x[i].append(center[0])
                            list_of_y[i].append(center[1])



                            
                    
                    if New_brick==True:
                        list_of_x.append([center[0]])
                        list_of_y.append([center[1]])
                        points=np.array(Cor)
                        ind = np.lexsort((points[:,0],points[:,1]))
                        Cor=Cor[ind]

                        p1x.append([Cor[0,0]])
                        p2x.append([Cor[1,0]])
                        p3x.append([Cor[3,0]])
                        p1y.append([Cor[0,1]])
                        p2y.append([Cor[1,1]])
                        p3y.append([Cor[3,1]])

                        
                        list_of_type.append(Brick_type)

                        avg_center_list_x.append([center[0]])
                        avg_center_list_y.append([center[1]])


                    
        for i in range(0,len(avg_center_list_x[:])):
            avg_center_list_x[i]=np.mean(list_of_x[i])
            avg_center_list_y[i]=np.mean(list_of_y[i])
            std_x=np.std(list_of_x[i])
            std_y=np.std(list_of_y[i])

            std_list=[std_x,std_y]
            if all(std<1 for std in std_list) and t>=1000 and list_of_type[i]==type:
                p1=[np.mean(p1x[i]),np.mean(p1y[i])]
                p2=[np.mean(p2x[i]),np.mean(p2y[i])]
                p3=[np.mean(p3x[i]),np.mean(p3y[i])]
                Angle=Mv_math.get_slope(p1,p2,p3,list_of_type[i])
                avg_angle=Angle
                print('Succes: The brick chosen was:' + str(i)+'    Which is type: '+str(list_of_type[i]))
                print('Which had the following deviations: X:'+str(std_x)+'  Y:'+str(std_y))
                print('Which had the following location: X:'+str( avg_center_list_x[i])+'  Y:'+str( avg_center_list_y[i])+'  Angle:'+str(avg_angle))
                print('And took ' +str(t)+' Frames to get')
                Found=True
                result_x=avg_center_list_x[i]
                result_y=avg_center_list_y[i]
                result_angle=avg_angle
                
                break
            elif t>=2000:
            
                print("No brick was found")
                Found=True
                break

        cv2.imshow('canny',cannyImg)
        cv2.imshow('out',img)
        if Found==True:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'): # q closes our webcam
            break
        #Counter checking the number of pictures taken
        t=t+1
    return result_x, result_y, result_angle
    #print('finished')
    #print(list_of_type)
    #print(list_of_x)
    #print(list_of_y)
    #print(list_of_angle)

if __name__ == '__main__':
    get_xyA(0,0)