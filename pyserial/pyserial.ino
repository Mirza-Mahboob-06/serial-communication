#!/usr/bin/enc python3
import rclpy
from rclpy.node import Node
from serial import Serial
from std_msgs.msg import String

class SerialReaderNode(Node):

    def __init__(self):
        super().__init__('com')

       
        self.serial_port = '/dev/ttyACM0'
        self.baud_rate = 9600

        self.serial = Serial(self.serial_port, self.baud_rate)

        self.publisher = self.create_publisher(String, 'serial_data', 10)
        self.timer = self.create_timer(0.1, self.read_serial_data)

    def read_serial_data(self):
        if self.serial.in_waiting > 0:
          data = self.serial.readline().decode('utf-8')
          self.publisher.publish(String(data=data))
        else:
          print("connection failed")

def main(args=None):
    rclpy.init(args=args)
    node = SerialReaderNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
