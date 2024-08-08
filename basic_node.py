import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('nameOfNode')
        self.get_logger().info('ROSsaysHEYtoPARV')

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
