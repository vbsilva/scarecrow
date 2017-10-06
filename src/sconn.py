import serial
import time

class SerialConnection(object):
      def __init__(self):
          self.port = "/dev/serial0"
          self.rate = 9600
          self.connection = serial.Serial(port,rate)

      def send_message(self,message):
          connection.write(message)
