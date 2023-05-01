# Repository for workshop project
Workshop project for the course Robot vision, on the 2. semester of the Masters programme in Mechanical Engineering with specialisation in Manufacturing Technolog, Aalborg university. The excercise consists of pick-and-place of LEGO bricks with a robot using machine vision to identify and locate the position of LEGO bricks. The repository includes both files for the robot and vision code, with corresponding file prefixes of RV and MV, respectively.

Masters programme information: https://studieordninger.aau.dk/2023/41/4114 

Video of the result https://www.youtube.com/watch?v=zrSkYkhCW_g

## Table of content
[Installation](#Installation)<br/>
[Dependensies](#Dependensies)<br/>
[How It Works](#How It Works)<br/>

# Dependensies
- OpenCV
- Numpy
- RoboDK


# How It Works
- Robot_main.py is the main code, it controls the robot through robolink and robodk. This is both used to simulate and run live with a simple input statement. It primarely works with a few targets, and reference frames. It will pause before any pick up or placement to ensure that the position is correct waiting for a user confirmation in the console. Both pickups and placements are given relative to a reference frame.

- MV.py is the main vision script. It masks out detected bricks by contours and colours via HSV masks and Otsu thresholding. A brick is found when a contour with 4 corners of a certain area size is detected, whereafter location, as well as the brick type and colour, are all noted. For the next contour, if the center location is within 20 pixels of another brick, then the same brick has been found, and new data is added in order to refine the location calculation. Otherwise, a new brick is detected. In summary, the script identifies and classificies bricks, and returns their positions.

- RV_Math.py defines two functions, used in support of the previously mentioned script. The first function identifies the type of the LEGO brick (either 2x2 or 2x4 studs) by computing the length of the sides and comparing ratios. The second function computes the angle of rotation of the brick by using slopes.

- mainRV.py converts the position data of a brick to the robot coordinate space, along with the type and colour.

- RV_transform.py defines the transformation function used in the previously mentioned script.

Note that some manual calbration is required, since some values depend on the physical setup, i.e. the robot cell. Among these are:
- image feed cropping (line 56 in MV.py)
- the area for the brick contrours (line 90 in MV.py)
- the upper and lower RGB-value limits (line 40-50 in MV.py), which specifies the colour ranges for the different brick colours.

### Physical dependencies

Camera. A specific camera is not required, however a Logitech 1920x1080 webcam camera was used.
