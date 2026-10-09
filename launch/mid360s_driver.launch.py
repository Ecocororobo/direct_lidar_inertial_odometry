"""Start the official Livox driver using this package's MID360S config."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    config = PathJoinSubstitution([
        FindPackageShare('direct_lidar_inertial_odometry'),
        'cfg', 'MID360s_config.json'])
    return LaunchDescription([
        DeclareLaunchArgument('user_config_path', default_value=config),
        DeclareLaunchArgument('xfer_format', default_value='0', choices=['0', '1']),
        DeclareLaunchArgument('publish_freq', default_value='10.0'),
        Node(
            package='livox_ros_driver2', executable='livox_ros_driver2_node',
            name='livox_lidar_publisher', output='screen',
            parameters=[{
                'xfer_format': ParameterValue(LaunchConfiguration('xfer_format'), value_type=int),
                'multi_topic': 0,
                'data_src': 0,
                'publish_freq': ParameterValue(LaunchConfiguration('publish_freq'), value_type=float),
                'output_data_type': 0,
                'frame_id': 'livox_frame',
                'user_config_path': LaunchConfiguration('user_config_path'),
                'cmdline_input_bd_code': 'livox0000000001',
                'lvx_file_path': '',
            }]),
    ])
