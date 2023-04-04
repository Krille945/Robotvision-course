
from ast import Try
import pyvista as pv
import numpy as np
import Reduce

def smart_overhang(list, array, order):
    list_of_solved_bricks=[]
    list_of_remaining=[]
    print(len(list))
    for i in range(0,len(list)):
        #check arround brick
        brick=list[i]
    
        if (brick[2]% 2)==0:
            if array[brick[0],brick[1]-1,brick[2]]==1:
                array[brick[0],brick[1]-1,brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0],brick[1]+1,brick[2]]==1:
                array[brick[0],brick[1]+1,brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0],brick[1]-1,brick[2]]==1 and array[brick[0],brick[1]-1,brick[2]]==1:
                array[brick[0],brick[1]-1,brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0]-1,brick[1],brick[2]]==1:
                array[brick[0]-1,brick[1],brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0]+1,brick[1],brick[2]]==1:
                array[brick[0]+1,brick[1],brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0]-1,brick[1],brick[2]]==1 and array[brick[0]+1,brick[1],brick[2]]==1:
                array[brick[0]-1,brick[1],brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            else:
                print("couldn't remove ")
                list_of_solved_bricks.append(0)
        else:
            if array[brick[0]-1,brick[1],brick[2]]==1:
                array[brick[0]-1,brick[1],brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0]+1,brick[1],brick[2]]==1:
                array[brick[0]+1,brick[1],brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0]-1,brick[1],brick[2]]==1 and array[brick[0]+1,brick[1],brick[2]]==1:
                array[brick[0]-1,brick[1],brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0],brick[1]-1,brick[2]]==1:
                array[brick[0],brick[1]-1,brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0],brick[1]+1,brick[2]]==1:
                array[brick[0],brick[1]+1,brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            elif array[brick[0],brick[1]-1,brick[2]]==1 and array[brick[0],brick[1]-1,brick[2]]==1:
                array[brick[0],brick[1]-1,brick[2]]=order
                array[brick[0],brick[1],brick[2]]=order
                list_of_solved_bricks.append(1)
                print("could remove ")
                order=order+ 1
            else:
                print("couldn't remove ")
                list_of_solved_bricks.append(0)

    #print(list_of_solved_bricks)
    for i in range(0,len(list)):
        if list_of_solved_bricks[i]==0:
            list_of_remaining.append(list[i])

    list=list_of_remaining
    print (list)

    #print(order)
    return list, array, order

               
def two_by_two_to_one_by_one(array):
    stud_array=np.zeros((2*len(array[:,1,1]),2*len(array[1,:,1]),len(array[1,1,:])))
    for i in range(0,len(array[1,1,:])):
        for t in range(0,len(array[1,:,1])):
            for k in range(0,len(array[:,1,1])):
                stud_array[k*2,t*2,i]=array[k,t,i]
                stud_array[k*2+1,t*2,i]=array[k,t,i]
                stud_array[k*2,t*2+1,i]=array[k,t,i]
                stud_array[k*2+1,t*2+1,i]=array[k,t,i]
    return stud_array

def convert(path):
    order = 2

    file_path = path

    stl_file = pv.read(file_path)

    center=stl_file.center

    bounds=stl_file.bounds



    stl_file.points+=[-center[0],-center[1],-bounds[4]+(-0.01)]

    #stl_file.scale([4.2,4.2,4.2])
    #stl_file.scale([8,8,8])
    #stl_file.scale([1,1,1])
    stl_file.scale([1,1,1])
    bounds=stl_file.bounds

    max=9.6*32.
    #checks bounds
    for i in range(0,len(bounds)):
        if bounds[i]**2>max**2:
            print('exceeds bounds of buildplate')
            break
        else:
            continue
    #stl_file.points+=[(224)/2,(192)/2-35,0]
    stl_file.points+=[(224)/2,(192)/2-4,0]

    min=0
    max_x=224
    max_y=192
    density_x=(224-8)/14
    density_y=(192-8)/12
    density_z=(max)/32
    x = np.arange(min+4, max_x-4, density_x)
    y = np.arange(min+4, max_y-4, density_y)
    z = np.arange(min, max, density_z)
    x, y, z = np.meshgrid(x, y, z)


    # Create unstructured grid from the structured grid
    grid = pv.StructuredGrid(x, y, z)
    ugrid = pv.UnstructuredGrid(grid)

    # get part of the mesh within the mesh's bounding surface.
    selection = ugrid.select_enclosed_points(stl_file.extract_surface(),
                                            tolerance=0.0,
                                            check_surface=False)
    mask = selection.point_data['SelectedPoints'].view(np.bool)

    plot= pv.Plotter()
    plot.add_mesh(grid.points, scalars=mask)

    voxels=pv.voxelize(stl_file,density_z)

    actor = plot.add_mesh(stl_file, color='red')

    def toggle(flag):
        actor.SetVisibility(flag)

    plot.add_checkbox_button_widget(toggle,value=True)

    plot.show_axes()
    plot.show_grid()

    block_array=np.zeros((14,12,32))
    g=0
    for i in range(0,32):
        for k in range(0,14):
            for t in range(0,12):
                if mask[g] == True:
                    block_array[k,t,i]=1
                g=g+1
        print("help")
        print(block_array[:,:,i])

    airlist=[]
    for i in range(1,len(block_array[1,1:])):
        for t in range(0,len(block_array[1,:,1])):
            for k in range(0,len(block_array[:,1,1])):
                if block_array[k,t,i] == 1:
                    if block_array[k,t,i-1] == 0:
                        air=[k,t,i]
                        airlist.append(air)
    before=np.count_nonzero(block_array)

    #airlist,block_array, order = smart_overhang(airlist, block_array, order)
    block_array, order = Reduce.reduce_bricks(block_array, order)
    stud_array=two_by_two_to_one_by_one(block_array)

    
    after=len(np.unique(block_array))-1
    print("Result of reduction: Before: "+str(before)+"  After: "+str(after))

    plot.show()
    np.savetxt("file_name"+str(0)+".csv", block_array[:,:,0], delimiter=",")

    return stud_array