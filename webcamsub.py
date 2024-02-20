import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from rclpy.qos import qos_profile_sensor_data

class ImageSubscriber(Node):
    def _init_(self, name):
        super()._init_(name)
        
        self.image_subscription = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            qos_profile=qos_profile_sensor_data)
        self.timer = self.create_timer(0.1, self.timer_callback)  # Set timer period to 0.1 seconds

        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(msg, 'bgr8')
            cv2.imshow('Camera Output', cv_image)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"Error processing camera image: {str(e)}")

    def timer_callback(self):
        # Additional logic that you want to run periodically
        pass

def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber(name='camera_subscriber')  
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()
