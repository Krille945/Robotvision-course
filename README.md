# Repository for workshop project
Workshop project for the course Robot vision, on the 2. semester of the Masters programme in Mechanical Engineering with specialisation in Manufacturing Technolog, Aalborg university. The project consists of pick-and-place of LEGO bricks with a robot using machine vision to identify and locate the position of LEGO bricks. The repository includes both files for the robot and vision code, with corresponding file prefixes of RV and MV, respectively.

Masters programme information: https://studieordninger.aau.dk/2023/41/4114 

## Table of content
[Installation](#Installation)<br/>
[Instructions to run](#Instructions)<br/>
[How it works](#HowItWorks)<br/>
[Known issues](#KnownIssues)<br/>


## Intallation
In root directory run:
```
pip install -r requirements.txt
```
gotta make that file ^^

## Instructions
In root directory run
```
kalibr
```
to obtain


# How It Works

- MV.py is the main script. It masks out detected bricks by contours and colours. A brick is found when a contour with 4 corners of a certain area size is detected, whereafter location, standard deviations, type and brick colour data noted. For the next contour, if the center location is within 20 pixels of another brick, then the same brick has been found, and new data is added in order to refine the location calculation. Otherwise, a new brick is detected. In summary, the script identifies and classificies bricks, and returns their positions.

- RV_Math.py defines two functions, used in support of the previously mentioned script. The first function identifies the type of the LEGO brick (either 2x2 or 2x4 studs) by computing the length of the sides and comparing ratios. The second function computes the angle of rotation of the brick by using slopes.

- mainRV.py converts the position data of a brickto the robot coordinate space, along with the type and colour.

- RV_transform.py defines the transformation function used in the previously mentioned script.

Note that some manual calbration is required, since some values depend on the physical setup. This includes:
- the area (line 91 in MV.py), which specifies the area in pixels that the contours can be, before ...
- the upper and lower RGB-value limits (line 42-53 in MV.py), which specifies the colour ranges for the different brick colours.

## Known issues

- issue 1

- issue 2

### Physical dependencies

Webcam. A specific webcam is not required, however the following was used for the robot cell: [name](https://google.com). Minimum of 1080p resolution, since the code creates 1000x1000 pixel image captures.