def reduce_bricks(array, order):
    orientation=0
    for i in range(0,len(array[1,1,:])):
        orientation=orientation+1
        if orientation==5:
            orientation=1
        
        if orientation==1:
            print("even1")
            for t in range(0,len(array[1,:,1])):
                    ends=[]
                    begins=[]
                    where_one=[k for k,x in enumerate(array[:,t,i]) if x==1]
                    for g in range(0,len(where_one)):
                        if where_one[g]-1 not in where_one[:]:
                            begins.append(where_one[g])
                        if where_one[g]+1 not in where_one[:]:
                            ends.append(where_one[g])
                        
                    for c in range(0,len(begins)):
                        number_of_2_by_4=(ends[c]-begins[c]+1)/2

                        if ends[c]==begins[c]:
                            array[int(begins[c]),t,i]=order
                            order =order +1
                        elif ((number_of_2_by_4-1.5)%2)==0:
                            middle=number_of_2_by_4-0.5
                            array[int(begins[c]+middle-1),t,i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four:
                                array[int(begins[c]+j),t,i]=order
                                array[int(begins[c]+j+1),t,i]=order
                                order =order +1
                                array[int(ends[c]-j-2),t,i]=order
                                array[int(ends[c]-j-1-2),t,i]=order
                                j=j+2
                                order =order +1
                            array[int(ends[c]),t,i]=order
                            array[int(ends[c]-1),t,i]=order
                            order =order +1
                        elif ((number_of_2_by_4-0.5)%2)==0:
                            middle=number_of_2_by_4+0.5
                            array[int(begins[c]+middle-1),t,i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four: 
                                array[int(begins[c]+j+1),t,i]=order
                                array[int(begins[c]+j),t,i]=order##
                                order =order +1
                                array[int(ends[c]-j-1),t,i]=order
                                array[int(ends[c]-j),t,i]=order##
                                j=j+2
                                order =order +1

                        else:
                            j=0
                            two_by_four=number_of_2_by_4

                            while j < 2*two_by_four:
                                array[int(begins[c]+j),t,i]=order
                                array[int(begins[c]+j+1),t,i]=order
                                order =order +1
                                j=j+2
            #print(array[:,:,i])


        elif orientation==2:
            print("odd1")
            for k in range(0,len(array[:,1,1])):
                    ends=[]
                    begins=[]
                    where_one=[t for t,x in enumerate(array[k,:,i]) if x==1]
                    for g in range(0,len(where_one)):
                        if where_one[g]-1 not in where_one[:]:
                            begins.append(where_one[g])
                        if where_one[g]+1 not in where_one[:]:
                            ends.append(where_one[g])

                    for c in range(0,len(begins)):
                        number_of_2_by_4=(ends[c]-begins[c]+1)/2
                        if ends[c]==begins[c]:
                            array[k,int(begins[c]),i]=order
                            order =order +1
                        elif ((number_of_2_by_4-1.5)%2)==0:
                            middle=number_of_2_by_4-0.5
                            array[k,int(begins[c]+middle-1),i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four:
                                array[k, int(begins[c]+j),i]=order
                                array[k, int(begins[c]+j+1),i]=order
                                order =order +1
                                array[k, int(ends[c]-j-2),i]=order
                                array[k, int(ends[c]-j-1-2),i]=order
                                j=j+2
                                order =order +1
                            array[k, int(ends[c]),i]=order
                            array[k, int(ends[c]-1),i]=order
                            order =order +1
                        elif ((number_of_2_by_4-0.5)%2)==0:
                            middle=number_of_2_by_4+0.5
                            array[k,int(begins[c]+middle-1),i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four:
                                array[k,int(begins[c]+j),i]=order
                                array[k,int(begins[c]+j+1),i]=order
                                order =order +1
                                array[k,int(ends[c]-j),i]=order
                                array[k,int(ends[c]-j-1),i]=order
                                j=j+2
                                order =order +1

                        else:
                            j=0
                            two_by_four=number_of_2_by_4

                            while j < 2*two_by_four:
                                array[k,int(begins[c]+j),i]=order
                                array[k,int(begins[c]+j+1),i]=order
                                order =order +1
                                j=j+2
            
        elif orientation==3:
            print("even2")
            for t in range(0,len(array[1,:,1])):
                    ends=[]
                    begins=[]
                    where_one=[k for k,x in enumerate(array[:,t,i]) if x==1]
                    for g in range(0,len(where_one)):
                        if where_one[g]-1 not in where_one[:]:
                            begins.append(where_one[g])
                        if where_one[g]+1 not in where_one[:]:
                            ends.append(where_one[g])
                        
                    for c in range(0,len(begins)):
                        number_of_2_by_4=(ends[c]-begins[c]+1)/2

                        if ends[c]==begins[c]:
                            array[int(begins[c]),t,i]=order
                            order =order +1
                        elif ((number_of_2_by_4-1.5)%2)==0:
                            middle=number_of_2_by_4-0.5
                            array[int(begins[c]+middle+1),t,i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four:
                                array[int(begins[c]+j+2),t,i]=order
                                array[int(begins[c]+j+1+2),t,i]=order
                                order =order +1
                                array[int(ends[c]-j),t,i]=order
                                array[int(ends[c]-j-1),t,i]=order
                                j=j+2
                                order =order +1
                            array[int(begins[c]),t,i]=order
                            array[int(begins[c]+1),t,i]=order
                            order =order +1
                        elif ((number_of_2_by_4-0.5)%2)==0:
                            middle=number_of_2_by_4+0.5
                            array[int(begins[c]+middle-1),t,i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < two_by_four*2: 
                                array[int(begins[c]+j),t,i]=order
                                array[int(begins[c]+j+1),t,i]=order
                                order =order +1
                                array[int(ends[c]-j),t,i]=order
                                array[int(ends[c]-j-1),t,i]=order
                                j=j+2
                                order =order +1

                        else:
                            j=0
                            two_by_four=number_of_2_by_4

                            while j < 2*two_by_four:
                                array[int(begins[c]+j),t,i]=order
                                array[int(begins[c]+j+1),t,i]=order
                                order =order +1
                                j=j+2

        elif orientation==4:
            print("odd2")
            for k in range(0,len(array[:,1,1])):
                    ends=[]
                    begins=[]
                    where_one=[t for t,x in enumerate(array[k,:,i]) if x==1]
                    for g in range(0,len(where_one)):
                        if where_one[g]-1 not in where_one[:]:
                            begins.append(where_one[g])
                        if where_one[g]+1 not in where_one[:]:
                            ends.append(where_one[g])

                    for c in range(0,len(begins)):
                        number_of_2_by_4=(ends[c]-begins[c]+1)/2
                        if ends[c]==begins[c]:
                            array[k,int(begins[c]),i]=order
                            order =order +1
                        elif ((number_of_2_by_4-1.5)%2)==0:
                            middle=number_of_2_by_4-0.5
                            array[k,int(begins[c]+middle+1),i]=order##fix was here
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four:
                                array[k, int(begins[c]+j+2),i]=order
                                array[k, int(begins[c]+j+1+2),i]=order
                                order =order +1
                                array[k, int(ends[c]-j),i]=order
                                array[k, int(ends[c]-j-1),i]=order
                                j=j+2
                                order =order +1
                            array[k, int(begins[c]),i]=order
                            array[k, int(begins[c]+1),i]=order
                            order =order +1
                        elif ((number_of_2_by_4-0.5)%2)==0:
                            middle=number_of_2_by_4+0.5
                            array[k,int(begins[c]+middle-1),i]=order
                            order =order +1
                            two_by_four=(middle-1)/2
                            j=0
                            while j < 2*two_by_four:
                                array[k,int(begins[c]+j),i]=order
                                array[k,int(begins[c]+j+1),i]=order
                                order =order +1
                                array[k,int(ends[c]-j),i]=order
                                array[k,int(ends[c]-j-1),i]=order
                                j=j+2
                                order =order +1

                        else:
                            j=0
                            two_by_four=number_of_2_by_4

                            while j < 2*two_by_four:
                                array[k,int(begins[c]+j),i]=order
                                array[k,int(begins[c]+j+1),i]=order
                                order =order +1
                                j=j+2
                    
        print(array[:,:,i]) 
    return array,order