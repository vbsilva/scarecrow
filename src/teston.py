import serial
import time
import struct
from subprocess import call


port = "/dev/serial0"
rate = 9600

connection = serial.Serial(port,rate)
j = 2

#source = Sensors()

time.sleep(1)

while(j != 0):
     #data = source.get_temp_n_hum()
     #temperature = data[0]
     #hum = data[1]
     #lum = source.get_lum()
     #rain = source.get_rain()
     #soil = source.get_soil()
     data = [50,86,33,49,34,35,36]
     time.sleep(1)
     for i in data:
          connection.write(struct.pack('>B', i))
     time.sleep(10)
     print("enviado ...",data)
     j = j - 1


connection.close()
#time.sleep(30)

#call("sudo shutdown now", shell=True)


