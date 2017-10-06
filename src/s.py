import serial
import time

port = "/dev/serial0"
rate = 9600

connection = serial.Serial(port,rate)

while(True):
     msg = [b'1234567890']
     connection.write(msg[0])
     print("enviado")
     time.sleep(2)
