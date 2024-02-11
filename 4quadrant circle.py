#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial
from turtlesim.srv import Spawn



class Turtlecontrollernode(Node):

    def _init_(self):
        super()._init_("Turtlecontroller")
        
        self.cmd_vel_pub_ =self.create_publisher(
            Twist,"/turtle2/cmd_vel",10)
        
        self.possubscriber_=self.create_subscription(
            Pose,"/turtle2/pose", self.pose_callback,10)
        self.get_logger().info("Turtle controller has been started")

    def pose_callback(self,pose:Pose):
        cmd=Twist()

        
        cmd.linear.x=2.0
        cmd.angular.z=1.0
        if pose.x >5.5 and pose.y >5.5:
            self.callsetpenservice(255,0,0,3,0)
        elif pose.x <5.5 and pose.y >5.5 :
            self.callsetpenservice(0,255,0,3,0)
            
            

        elif pose.x <5.5 and pose.y <5.5 :
            self.callsetpenservice(100,155,0,3,0)
            
            
        elif pose.x >5.5 and pose.y <5.5:
            self.callsetpenservice(0,255,255,3,0)
        
        
        self.cmd_vel_pub_.publish(cmd)


    def callsetpenservice(self,r,g,b,width,off):
        client=self.create_client(SetPen,"/turtle2/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")

        request = SetPen.Request()
        request.r=r
        request.g=g
        request.b=b
        request.width=width
        request.off=off

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    


    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))


# ... (remaining code)

def main(args=None):
    rclpy.init(args=args)
    node = Turtlecontrollernode()
    rclpy.spin(node)
    rclpy.shutdown()
