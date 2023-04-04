import numpy as np

def measure_rigid(array):
    brickval=np.max(array)
    #print(brickval)
    t=2
    number_seams=0
    tt=0
    while t<=brickval:
        print("start")
        x = np.where(array == t)[0]
        y =np.where(array == t)[1]
        z =np.where(array == t)[2]
        print(x,y,z)
        #print(t)

        if z.size==0:
            print(t)
        elif np.all(z) != 0:
            num_unique=np.unique(array[x[:],y[:],z[1]-1])
            non_zero=len(num_unique)
            if 0 in array[x,y,z[1]-1]:
                non_zero=non_zero-1
            #print(non_zero)
            tt=tt+1
            number_seams=number_seams+non_zero
        

        
        t=t+1
    number_div=(number_seams/tt)/2
    return number_div


        
