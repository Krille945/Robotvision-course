from gettext import translation
import numpy as np


def gen_instructions(array,support):
    minval=np.min(array[np.nonzero(array)])
    maxval=np.max(array[np.nonzero(array)])
    t=minval
    bricknumber=1
    list_of_bricks=[]
    list_of_movetypes=[]
    counter=[]
    output=np.zeros(7)
    #interval=maxval-minval
    while t<=maxval:
        x = np.where(array == t)[0]
        y = np.where(array == t)[1]
        z = np.where(array == t)[2]
        print(x,y,z)

        center_x=np.mean(x)
        center_y=np.mean(y)
        center_z=np.mean(z)
        if z.size==0:
            print(t)
        elif np.max(x)-np.min(x)==3:
            angle=90
            type=2
            # type=3001
        elif np.max(y)-np.min(y)==3:
            type=2
            #type=3001
            angle=0
        else:
            angle=0
            #type=0
            if t>support:
                type=0
            else:
                type=1
        
        list_of_bricks.append([center_x,center_y, center_z,angle,t,type])
        t=t+1
        bricknumber=bricknumber+1

    list_of_bricks=np.array(list_of_bricks)

    #ind = np.lexsort((-list_of_bricks[:,0],list_of_bricks[:,1],list_of_bricks[:,2]))
    #Sorted_array=list_of_bricks[ind]
    ind = np.lexsort((list_of_bricks[:,4],list_of_bricks[:,2]))
    print(ind)
    Sorted_z_array=list_of_bricks[ind]
    print(Sorted_z_array)
    
    Sorted_z_array=np.array(Sorted_z_array)
    unique_z_layers=np.unique(Sorted_z_array[:,2])
    Sorted_array=np.zeros(6)
    print("unique")
    #print(unique_z_layers)
    print("test")
    #print(Sorted_z_array)
    #list_test=Sorted_z_array[1,:]
    for i in range(0,len(unique_z_layers)):
        list_test=Sorted_z_array[:,2]
        #print(list_test)
        z = np.where(list_test == i)[0]
        if z.size==0:
            break
        min_Z=np.min(z)
        print(z)
        temp_array=Sorted_z_array[z,:]
        print(i)
        if ((i-1)% 2)!=0:
            print("even")
            print(temp_array)
            ind = np.lexsort((-temp_array[:,0],temp_array[:,1]))
            layer=Sorted_z_array[ind+min_Z]
            
        elif ((i-1)% 2)==0:
            print("odd")
            print(temp_array)
            ind = np.lexsort((temp_array[:,1],-temp_array[:,0]))
            layer=Sorted_z_array[ind+min_Z]



        Sorted_array=np.vstack([Sorted_array,layer])
        
    Sorted_array = np.delete(Sorted_array, 0, 0)
    print(Sorted_array)
    translation=Sorted_array[:,4]
    #print (translation)
    for i in range(0,len(translation)):
        counter.append(i+1)
        x = np.where(array == translation[i])[0]
        y = np.where(array == translation[i])[1]
        z = np.where(array == translation[i])[2]
        #print("movetest")
        unique_x=np.unique(x)
        unique_y=np.unique(y)
        max_x=np.max(x)+1
        min_y=np.min(y)-1
        max_y=np.max(y)+1
        min_z=np.min(z)
        #print(unique_x)
        #print(unique_y)

        if_y=False
        if_x=False
        if_any_support=False

        #print("min_z")
        #print(len(unique_x))
        if min_y>=0:
            #print("array val")
            
            for t in range(0,len(unique_x)):
                #where=np.where(translation == int(array[unique_x[t],min_y,min_z]))[0]
                where=np.where(translation == int(array[unique_x[t],min_y,min_z]))[0]
                #print("i and where")
                #print(i)
                #print(where)
                if where<i and translation[where]>support:
                    if_any_support=True
                    if_x=True
                elif where<i:
                    if_x=True
            for t in range(0,len(unique_y)):
                #print("i and where")
                #print(i)
                #print(where)
                where=np.where(translation == int(array[max_x,unique_y[t],min_z]))[0]
                if where<i and translation[where]>support:
                    if_any_support=True
                    if_y=True
                elif where<i:
                    if_y=True
        if if_y==True and if_x==True and if_any_support==True:
            movetype=5
        elif if_y==False and if_x==True and if_any_support==True:
            movetype=6
        elif if_y==True and if_x==False and if_any_support==True:
            movetype=7        
        elif if_y==False and if_x==False and if_any_support==False:
            movetype=1
        elif if_y==True and if_x==True and if_any_support==False:
            movetype=2
        elif if_y==False and if_x==True and if_any_support==False:
            movetype=3
        elif if_y==True and if_x==False and if_any_support==False:
            movetype=4

        list_of_movetypes.append(movetype)
    
    for i in range(0,len(Sorted_array[:,0])):
        #dy=(8)
        dy=8
        #dy=8
        dx=7.9777777
        #dx=(8-0.06571428)
        #dx=(8-0.08401)
        dz=9.6
        #dz=9.5
        T=np.array([[0,-1,0,515.56],[1,0,0,-106.9],[0, 0, 1, 141.8],[0, 0, 0, 1]])
        #T=np.array([[0,-1,0,(515.56)],[1,0,0,-106.15],[0, 0, 1, 141.38],[0, 0, 0, 1]])
        #T=np.array([[0,-1,0,(516.45)],[1,0,0,-110.23],[0, 0, 1, 143.04],[0, 0, 0, 1]])
        studs_list=[Sorted_array[i,0],Sorted_array[i,1],Sorted_array[i,2]]
        studs_to_mm=[Sorted_array[i,0]*dx,Sorted_array[i,1]*dy,Sorted_array[i,2]*dz,1]
        
        #in_robot_coords=T.dot(studs_to_mm)
        in_robot_coords=studs_to_mm
        #in_robot_coords=compensator.compensate(studs_list,in_robot_coords)
        #step=[in_robot_coords[0]-4,in_robot_coords[1]-12,in_robot_coords[2],Sorted_array[i,3],list_of_movetypes[i],i+1,Sorted_array[i,5]]
        step=[in_robot_coords[0]+4,in_robot_coords[1]-12,in_robot_coords[2],Sorted_array[i,3],list_of_movetypes[i],i+1,Sorted_array[i,5]]

        ## DU HAR FJERNET SAFETY
        #if any(studs_to_mm[0:1]) > 32*dxy or studs_to_mm[3] > 32*dz :
        #    print("Error out of bounds")
        #    break
        output=np.vstack([output,step])

    step=[0,0,0,0,0,0,0]
    output=np.vstack([output,step])
    #output=np.array([Sorted_array[:,0],Sorted_array[:,1],Sorted_array[:,2],Sorted_array[:,3],list_of_movetypes,counter])
    return output
        
                
















