# Repository for workshop project
Workshop project for the course Robot vision, on the 2. semester of the Masters programme in Mechanical Engineering with specialisation in Manufacturing Technolog, Aalborg university. The excercise consists of pick-and-place of LEGO bricks with a robot using machine vision to identify and locate the position of LEGO bricks. The repository includes both files for the robot and vision code, with corresponding file prefixes of RV and MV, respectively.

Masters programme information: <https://studieordninger.aau.dk/2023/41/4114> 

The workshop code is a further development of work previously done in a bachelor's thesis project. A video showcase can be found here: <https://youtu.be/XQf0FIjfyzM>. In summary, instruction sets for the robot could be generated automatically through either STL or LXFML files (LEGO structures created digitally in Studio 2.0). The differences with this workshop is an added ability to detect colours in the LXFML parser, and the integration between the vision and robot code.

# How It Works

- MV.py is the main script. It masks out detected bricks by contours and colours via HSV masks and Otsu thresholding. A brick is found when a contour with 4 corners of a certain area size is detected, whereafter location, as well as the brick type and colour, are all noted. For the next contour, if the center location is within 20 pixels of another brick, then the same brick has been found, and new data is added in order to refine the location calculation. Otherwise, a new brick is detected. In summary, the script identifies and classificies bricks, and returns their positions.

- RV_Math.py defines two functions, used in support of the previously mentioned script. The first function identifies the type of the LEGO brick (either 2x2 or 2x4 studs) by computing the length of the sides and comparing ratios. The second function computes the angle of rotation of the brick by using slopes.

- mainRV.py converts the position data of a brick to the robot coordinate space, along with the type and colour.

- RV_transform.py defines the transformation function used in the previously mentioned script.

Note that some manual calbration is required, since some values depend on the physical setup, i.e. the robot cell. This includes:
- the area (line 91 in MV.py), which specifies the area in pixels that the contours can be, before ...
- the upper and lower RGB-value limits (line 42-53 in MV.py), which specifies the colour ranges for the different brick colours.

Kalibrate_HSV can be run as an aid to calibrate the HSV values in MV.py

## Known issues

- issue 1

- issue 2

### Physical dependencies

Webcam. A specific webcam is not required, however the following was used for the robot cell: [name](https://google.com). Currently, the code crops the captured camera feed into a resolution of 1000x1000.
