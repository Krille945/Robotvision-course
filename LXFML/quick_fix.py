
def fix(instructions):

    for i in range(0,len(instructions[:,1])):
        if instructions[i,3]==-90:
            #print("test")
            #print(instructions[i,:])
            instructions[i,0]=instructions[i,0]-0.2
            instructions[i,1]=instructions[i,1]-0.5
            #print(instructions[i,:])
    
    return(instructions)


