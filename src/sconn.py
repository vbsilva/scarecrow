import serial
import time
import struct

class SerialConnection(object):
      def __init__(self):
          self.port = "/dev/serial0"
          self.rate = 9600

      def send_message(self,message):
          for i in message:
          	self.connection.write(struct.pack('>B', i))	
          time.sleep(10)
          for i in message:
            self.connection.write(struct.pack('>B', i))

      def close_conn(self):
      	   self.connection.close()

      def open_conn(self):
      	   self.connection = serial.Serial(self.port,self.rate)