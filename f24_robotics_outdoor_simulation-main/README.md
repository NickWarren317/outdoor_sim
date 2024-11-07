<h1> How to Turn on and Off street lights </h1>
<p> 1. Navigate to the outdoor_sim.wbt file and find the objects named "ControlledStreetLight" </p>
<p> 2. For the light to be on, change the beam width up, to turn it off, set it to 0</p>

<h1> Changing the Stoplight settings </h1>
<p> 1. Go to the outdoor_sim.wbt, find objects named "TrafficLight" here you can manipulate the red and green
light times </p>

<h1> How to run the simulation </h1>

<p> 0. Clone this repository "https://github.com/NickWarren317/f24_robotics_outdoor_simulation" </p>
<p> 1. Navigate to the f24_robotics_outdoor_simulation directory</p>
<p> 2. Perform a colcon build then source the install/setup.bash file </p>
<p> 3. Enter "source /opt/ros/humble/setup.bash" to source the ros setup</p>
<p> 4. From here enter "ros2 launch f24_robotics__outdoorsimulation launch.py" to run the simulation </p>

<h3> NOTE: The model is quite large, it is reconmended to lower the openGL graphics settings for better performance </h3>