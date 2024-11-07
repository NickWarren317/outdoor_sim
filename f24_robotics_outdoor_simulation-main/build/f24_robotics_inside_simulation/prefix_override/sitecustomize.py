import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nwarren317/ros2_ws/rcwest_inside/f24_robotics_inside_simulation/f24_robotics_inside_simulation/install/f24_robotics_inside_simulation'
