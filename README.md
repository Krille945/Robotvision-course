# Repository for workshop project
Workshop project for the course Robot vision, on the 2. semester of the Masters programme in Mechanical Engineering with specialisation in Manufacturing Technolog, Aalborg university. The excercise consists of pick-and-place of LEGO bricks with a robot using machine vision to identify and locate the position of LEGO bricks. The repository includes both files for the robot and vision code, with corresponding file prefixes of RV and MV, respectively.

Masters programme information: <https://studieordninger.aau.dk/2023/41/4114> 

The workshop code is a further development of work previously done in a bachelor's thesis project. A video showcase can be found here: <https://youtu.be/XQf0FIjfyzM>. In summary, instruction sets for the robot could be generated automatically through either STL or LXFML files (LEGO structures created digitally in Studio 2.0). The differences with this workshop is an added ability to detect colours in the LXFML parser, and the integration between the vision and robot.

# How It Works

- MV.py is the main script. It masks out detected bricks by contours and colours via HSV masks and Otsu thresholding. A brick is found when a contour with 4 corners of a certain area size is detected, whereafter location, as well as the brick type and colour, are all noted. For the next contour, if the center location is within 20 pixels of another brick, then the same brick has been found, and new data is added in order to refine the location calculation. Otherwise, a new brick is detected. In summary, the script identifies and classificies bricks, and returns their positions.
- RV_Math.py defines two functions, used in support of the previously mentioned script. The first function identifies the type of the LEGO brick (either 2x2 or 2x4 studs) by computing the length of the sides and comparing ratios. The second function computes the angle of rotation of the brick by using slopes.
- Robot_main.py uses the RoboDK API or Python to run the robot - the movement types and program.
- RV_transform.py defines the transformation function used to convert position data of the brick to the robot coordinate space.

Note that manual calibration is required, since some values depend on the physical setup, i.e. the robot cell. This includes:
- the area (MV.py), which specifies the area in pixels that the contours can envelop
- the upper and lower RGB-value limits (MV.py), which specifies the colour ranges for the different brick colours. Highly dependent on the robot cell. 
- width and height of camera capture, and cropping (MV.py)

## Known issues

- Ratios are used to detect the brick types, for instance if the ratio of side lengths is 1:1, then a 2x2 brick is detected. The camera is required to look straight down on the bricks, so problems may occur the more that the camera sees the sides of the brick as well.

### Physical dependencies

Webcam. A specific webcam is not required, however a 1920x1080 webcam was used.
