
%expected values
x_expected=[512.45 512.45 512.45-(24*8) 512.45-(24*8) 512.45 512.45 512.45-(24*8) 512.45-(24*8)]
y_expected=[-107.5 -107.5+(28*8) -107.5+(28*8) -107.5 -107.5 -107.5+(28*8) -107.5+(28*8) -107.5]
z_expected=[143.04 143.04 143.04 143.04 440.64 440.64 440.64 440.64]

%measured
x_measured=[512.45 512.45 320.45 320.45 510.7 511.78 324.21 322.65]
y_measured=[-107.5 106.66 106.66 -106.25 -107.99 104.38 105.22 -107.5]
z_measured=[143.04 143.04 143.04 143.04 437.99 437.99 437.99 437.99]

bounds_x=300:0.001:520;
bounds_y=-110:0.001:110;
bounds_z=140:0.001:450;
bounds_error=-25:0.001:25;
%error
x_error=x_expected-x_measured
y_error=y_expected-y_measured
z_error=z_expected-z_measured

%error in x as result of x-y
points_x=[x_expected(:), y_expected(:),z_expected(:), x_error(:)]
V_x=interpn(bounds_x,bounds_y,bounds_z,bounds_error,points_x,'cubic');

mesh(V_x);
%error in y as result of x-y
points_y=[x_expected(:), y_expected(:),z_expected(:), y_error(:)]

V_y=interpn(bounds_x,bounds_y,bounds_z,bounds_error,points_y,'cubic');

mesh(V_y);

