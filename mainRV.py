import MV
import RVTransform

#Type=1 is 2x2
#Type=2 is 2x4
type = 1
colour = 2

x,y,A=MV.get_xyA(type,colour)
Coords,Angle=RVTransform.Transform(x,y,A)

print('\nThe Results are then:')
print('Cords:'+str(Coords))
print('Angle:'+str(Angle))