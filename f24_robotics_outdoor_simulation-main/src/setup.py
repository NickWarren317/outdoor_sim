from setuptools import find_packages, setup

package_name = 'f24_robotics_outdoor_simulation'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/outdoor_sim.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='nwarren317',
    maintainer_email='yoitsbiggiecheese@gmail.com',
    description='Simulation of Downtown Tuscaloosa',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension' : ['launch_ros = launch_ros'],
        #'console_scripts': ['f24_robotics_inside_simulation = f24_robotics_inside_simulation.f24_robotics_inside_simulation:main'
        #],
    },
)
