import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
	    Node(
	      package='ldlidar_stl_ros2',
	      executable='ldlidar_stl_ros2_node',
	      name='STL27L',
	      output='screen',
	      parameters=[
	        {'product_name': 'LDLiDAR_STL27L'},
	        {'topic_name': 'scan'},
        	{'frame_id': 'base_laser'},
	        {'port_name': '/dev/ttyUSB0'},
	        {'port_baudrate': 921600},
	        {'laser_scan_dir': False},
	        {'enable_angle_crop_func': False},
	        {'angle_crop_min': 0.0},
	        {'angle_crop_max': 0.0}
	      ]
	    ),

            Node(
                package='rf2o_laser_odometry',
                executable='rf2o_laser_odometry_node',
                name='rf2o_laser_odometry',
                output='screen',
                parameters=[{
                    'laser_scan_topic' : '/scan',
                    'odom_topic' : '/odom_rf2o',
                    'publish_tf' : True,
                    'base_frame_id' : 'base_link',
                    'odom_frame_id' : 'odom',
                    'init_pose_from_topic' : '',
                    'freq' : 20.0}],
            ),
    ])
