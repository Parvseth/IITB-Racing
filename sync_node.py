import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from message_filters import Subscriber, ApproximateTimeSynchronizer

class SyncNode(Node):
    def __init__(self):
        super().__init__('sync_node')
        self.left_sub = Subscriber(self, Image, '/zed_left/zed_node_0/left/B')
        self.right_sub = Subscriber(self, Image, '/zed_right/zed_node_1/left/D')

        self.ats = ApproximateTimeSynchronizer([self.left_sub, self.right_sub], queue_size=10, slop=0.01)
        self.ats.registerCallback(self.callback)

    def callback(self, left_image, right_image):
        self.get_logger().info("Synchronized frames received")
        # Process synchronized images here

def main(args=None):
    rclpy.init(args=args)
    node = SyncNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

