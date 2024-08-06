import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from collections import deque
from rclpy.time import Time

class ManualSyncNode(Node):
    def __init__(self):
        super().__init__('manual_sync_node')
        self.left_buffer = deque()
        self.right_buffer = deque()

        self.left_sub = self.create_subscription(Image, '/zed_left/zed_node_0/left/B', self.left_callback, 10)
        self.right_sub = self.create_subscription(Image, '/zed_right/zed_node_1/left/D', self.right_callback, 10)

    def left_callback(self, msg):
        self.left_buffer.append(msg)
        self.try_synchronize()

    def right_callback(self, msg):
        self.right_buffer.append(msg)
        self.try_synchronize()

    def try_synchronize(self):
        if not self.left_buffer or not self.right_buffer:
            return

        left_msg = self.left_buffer[0]
        right_msg = self.right_buffer[0]

        time_diff = abs(left_msg.header.stamp.sec + left_msg.header.stamp.nanosec * 1e-9 -
                        right_msg.header.stamp.sec - right_msg.header.stamp.nanosec * 1e-9)

        if time_diff < 0.1:  # Tolerance in seconds
            self.left_buffer.popleft()
            self.right_buffer.popleft()
            self.get_logger().info("Manually synchronized frames received")
            # Process synchronized images here

def main(args=None):
    rclpy.init(args=args)
    node = ManualSyncNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
