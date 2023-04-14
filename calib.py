#Callibaration
import RV_Math
import numpy as np

x1=476.490099009901
y1=212.5
C_1=0.8842042008443652

x2=822.5173267326733
y2=526.8589108910891
C_2=4.5214365910576


result_x=[x1,x2]
result_y=[y1,y2]

result_angle=[C_1,C_2]

length_mm=100 #in mm
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
