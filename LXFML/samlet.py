from tkinter import filedialog
import numpy as np

#our own libraries 
import lxfml
import stl
import rigidity
import air_and_support
import create_instructions
import quick_fix

file_path = filedialog.askopenfilename(initialdir="/Examples")

file_type=file_path.split(".")[-1]

print(file_type)

if file_type == "lxfml":
    #stud_array=lxfml.convert(file_path)
    stud_array=lxfml.convert(file_path)
elif file_type == "stl":
    stud_array=stl.convert(file_path)
else:
    print("Error wrong filetype")



num=rigidity.measure_rigid(stud_array)
stud_array,support=air_and_support.air_support(stud_array)
instructions=create_instructions.gen_instructions(stud_array,support)
instructions=quick_fix.fix(instructions)## sørg for at fjern
print("rigidity indeks: "+str(num))

#file_number= len(os.listdir("Cvs_folder"))
file_number=0
instructions = np.delete(instructions, (0), axis=0)
file_name="generated_instructions"

np.savetxt(file_name+str(0)+".csv", instructions, delimiter=",")

#shutil.move(file_name+str(0)+".csv", "Cvs_folder/"+file_name+str(file_number)+".csv")
print(instructions)

print("resulting array")
#for i in range(0,len(stud_array[1,1,:])):
#    print("layer"+str(len(stud_array[1,1,:])))
#    print("layer"+str(i))
#    for t in range(0,len(stud_array[1,:,1])):
#        print(stud_array[:,t,i])
#print(stud_array)