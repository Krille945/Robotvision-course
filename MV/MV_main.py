import MV_contours
import Transform

#Type=1 is 2x2
#Type=2 is 2x4
type = 2
colour = 1

x,y,A=MV_contours.get_xyA(type,colour)
Coords,Angle=Transform.Transform(x,y,A)

print('\nThe Results are then:')
print('Cords:'+str(Coords))
print('Angle:'+str(Angle))