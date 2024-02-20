from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    drawcircle = Node(
        package="myrobocontroller",
        executable="drawcircle"
    )

    possubscriber = Node(
        package="myrobocontroller",
        executable="possubscriber"
    )

    turtlesim = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    ld.add_action(drawcircle)
    ld.add_action(possubscriber)
    ld.add_action(turtlesim)

    return ld
