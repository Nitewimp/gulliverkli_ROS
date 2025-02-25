import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node



def generate_launch_description():

    package_name='gulliverkli'

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    # Micro-ROS agent node
    micro_ros_agent = Node(
        package="micro_ros_agent",
        executable="micro_ros_agent",
        arguments=["serial", "--dev", "/dev/ttyUSB0", "--baudrate", "921600"],
        output="screen"
    )

    # joystick = IncludeLaunchDescription(
    #             PythonLaunchDescriptionSource([os.path.join(
    #                 get_package_share_directory(package_name),'launch','joystick.launch.py'
    #             )])
    # )


    



    # Launch them all!
    return LaunchDescription([
        rsp,
        micro_ros_agent,
        # joystick,
        
    ])