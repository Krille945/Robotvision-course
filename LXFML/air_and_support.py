import numpy as np

def air_support(array):
    print("zero bricks")
    air=[]
    brickval=np.max(array)
    order=brickval+1
    print(brickval)
    t=2
    number_seams=0
    tt=0
    while t<=brickval:
        x = np.where(array == t)[0]
        y =np.where(array == t)[1]
        z =np.where(array == t)[2]
        z_1=z-1
        if z.size==0:
            print(t)
        elif z.all()>=1:

            if np.all((array[x,y,z_1]==0)):
                print("flagged")
                print("brick: "+str(t))
                print(x,y,z)
                print(array[x,y,z_1])
                z_beneath=z_1
                while np.all((array[x,y,z_beneath]==0)) and np.all((z_beneath>=0)):
                    print("z beneath")
                    print(z_beneath)
                    
                    if len(np.unique(y))>=4:
                        array[x[2],y[2],z_beneath[1]]=order
                        array[x[3],y[3],z_beneath[2]]=order
                        array[x[6],y[6],z_beneath[5]]=order
                        array[x[7],y[7],z_beneath[6]]=order
                    elif len(np.unique(x))>=4:
                        array[x[4],y[4],z_beneath[1]]=order
                        array[x[5],y[5],z_beneath[2]]=order
                        array[x[6],y[6],z_beneath[5]]=order
                        array[x[7],y[7],z_beneath[6]]=order
                    else:
                        array[x,y,z_beneath]=order
                    print("placed: "+str(order))
                    print(x,y,z_beneath)
                    order=order+1
                    z_beneath=z_beneath-1
                
                print("the brick beneath:")
                print(array[x,y,z_beneath])

        t=t+1
    return array, brickval