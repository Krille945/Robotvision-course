
import numpy as np

def convert(file_path):


    brick_list=[]
    transformation_list=[]
    brick_ids=[]
    transformations=[]

    placement_lego_list=[]
    angle_list=[]



    ###read
    with open(file_path,'r') as f:
        data =f.read()
        data_list=data.splitlines()
        for t in range(0, len(data_list)):
            if "Brick refID" in data_list[t]:
                brick_list.append(data_list[t])
            elif "Bone refID" in data_list[t]:
                transformation_list.append(data_list[t])

        for t in range(0 , len(brick_list)):
            cur_string = brick_list[t]
            start = cur_string.find("designID=\"")+10
            end = cur_string.find("\" itemNos=")
            brick_ids.append(int(cur_string[start:end]))

        for t in range(0 , len(transformation_list)):
            cur_string = transformation_list[t]
            start = cur_string.find("transformation=\"")+16
            end = cur_string.find("\" />")
            transformations.append(cur_string[start:end])

    dxy=0.8
    dz=0.96
    ### transform to LEGO cords
    for t in range(0, len(transformations)):
        transformationvector=transformations[t].split(",")

        transformationvector=list(map(float,transformationvector))

        transformationvector_xzy=transformationvector[9:]

        transformationvector_lego=[transformationvector_xzy[0]/dxy,transformationvector_xzy[2]/dxy,transformationvector_xzy[1]/dz]

        transformationvector_lego=np.round(transformationvector_lego[:],3)
        print("transformationvector")
        print(transformationvector[0])
        if int(np.round(transformationvector[0],0))==0:
            angle =90
        else:
            angle = 0
        
        #print (angle)
        angle_list.append(angle)
        if angle==0:#VIGTIG CHECK
            angle=0.
        elif angle==90:
            angle=90.

        addedx=5
        addedy=5
        placement=[transformationvector_lego[0]+ addedx, -transformationvector_lego[1]+ addedy, transformationvector_lego[2] , angle, brick_ids[t]]
        #print(placement)
        placement_lego_list.append(placement)

    ## nu istedet for at stole på rækkefølgen man selv har valgt at sætte det så sorteres de efter xy placeringen
    placement_lego_list=np.array(placement_lego_list)
    ind = np.lexsort((placement_lego_list[:,0],placement_lego_list[:,1],placement_lego_list[:,2]))

    Sorted_array=placement_lego_list[ind]
    print(Sorted_array)

    block_array=np.zeros((14*2,12*2,32))

    for i in range(0,len(Sorted_array[:,1])):
        t=i+2
        if Sorted_array[i,4]==3001:
            if Sorted_array[i,3]==0:
                block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]+0.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]+0.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t

                block_array[int(Sorted_array[i,0]+2.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]+2.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]+1.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]+1.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t

            elif Sorted_array[i,3]==90:
                block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-1.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-1.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t

                block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]+2.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]+1.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-1.5),int(Sorted_array[i,1]+2.5),int(Sorted_array[i,2])]=t
                block_array[int(Sorted_array[i,0]-1.5),int(Sorted_array[i,1]+1.5),int(Sorted_array[i,2])]=t


        elif Sorted_array[i,4]==3003:
            block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
            block_array[int(Sorted_array[i,0]-0.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t
            block_array[int(Sorted_array[i,0]+0.5),int(Sorted_array[i,1]-0.5),int(Sorted_array[i,2])]=t
            block_array[int(Sorted_array[i,0]+0.5),int(Sorted_array[i,1]+0.5),int(Sorted_array[i,2])]=t
    return block_array













    