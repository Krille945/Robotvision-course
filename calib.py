#Callibaration
import RV_Math
import numpy as np

x1=304.99
y1=51.98
C_1=3.35

x2=727.22
y2=358.74
C_2=2.44


result_x=[x1,x2]
result_y=[y1,y2]

result_angle=[C_1,C_2]

#robot cords

xy_upper=[328.06,-144.35]
xy_lower=[546.00,155.87]

length_mm=RV_Math.calc_length(xy_upper,xy_lower)
length_px=RV_Math.calc_length(result_x,result_y)
mm_pr_px=length_mm/length_px
T_to_brick_x=100 #in mm
T_to_brick_y=100 #in mm
i_min=0

print('test')
print(result_x)
print(result_y)
print('The average angle of the brick is: '+str(np.mean(result_angle)))
print('The mm per pixel is: ' + str(mm_pr_px))
print('The first found brick had the following coordinates [x,y] in px: ' + str([result_x[i_min],result_y[i_min]]))
print('The first found brick had the following offset from [0,0] [x,y] in mm: ' + str([result_x[i_min]*mm_pr_px,result_y[i_min]*mm_pr_px]))
print('To [0,0] then has the following transformation [x,y,C]: '+str([T_to_brick_x-result_x[i_min]*mm_pr_px,T_to_brick_y-result_y[i_min]*mm_pr_px, np.mean(result_angle)]))
