clc
clear all

SE=[318.8; -114.28; 135.7];
SW=[318.8; 114.82; 134.72];
NW=[512.29; 114.17; 134.27];
NE=[511.45; -115.8; 134.33+8.71];

%NE1=[512.45; -107;134.33+8.71]
NE1=[512.45; -106.23;134.33+8.71]
%Robot to plate
T1=transl(NE1)*trotz((1/2)*pi)


%adjusted to the corner stud since the points were gained by 
test=[-4;-4; 0; 1]

Test=(T1*test)

Vector_to_zero=[516.45; -110.23; 143.04];

%Robot to plate
T=transl(Vector_to_zero)*trotz((1/2)*pi)

trplot(T); tranimate(T)
