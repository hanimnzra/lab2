import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        # First publisher
        self.publisher = self.create_publisher(String, 'chatter', 10)
        # Second publisher
        self.publisher2 = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0

    def talker_callback(self):
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
               
        msg2 = Int8()
        msg2.data = self.counter % 128
        self.publisher2.publish(msg2)
        self.get_logger().info(f'Publishing: {msg2.data}')
        
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    talker = Talker()
    rclpy.spin(talker)


if __name__ == '__main__':
    main()


