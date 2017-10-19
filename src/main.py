import os
import time
import cv2
import numpy as np
from sensors import Sensors
from imgprocessing import ImgProcessing
from sconn import SerialConnection

'''
    This is the main Module of the program
'''

def send_message(data,sigfox):
    sigfox.send_message(data)

def main():
    '''
        Main Function of the program
    '''
    #print("Scarecrow starting...")
    #print("Loading Sensors")
    source = Sensors()
    sigfox = SerialConnection()
    time.sleep(0.1)
    print("Loading AIModel")
    img_handler = ImgProcessing(camera=0,debug=False)
    print("AI Model loaded")
    while(True):
        try:
            sigfox.open_conn()
            data = source.get_temp_n_hum()
            temperature = data[0]
            humidity = data[1]
            luminosity = source.get_lum()
            if luminosity >= 20000:
                luminosity = 0
            elif luminosity >= 10000:
                luminosity = 1
            elif luminosity >= 5000:
                luminosity = 2
            else:
                luminosity = 3
            rain = source.get_rain()
            if rain >= 5000:
                rain = 1
            else:
                rain = 0
            soil = source.get_soil()
            if soil >= 20000:
                soil = 0
            elif soil >= 17000:
                soil = 1
            elif soil >= 100:
                soil = 2    
            bugs = img_handler.process_image(source)
            print(bugs)
            data = [int(temperature),int(humidity),100,luminosity,bugs,rain,soil]
            print(data)
            send_message(data,sigfox)
            sigfox.close_conn()
            source.blueLed()
            img_handler.capture.release()
        except KeyboardInterrupt:
            print("flw")
            GPIO.cleanup()
    
        time.sleep(5)
    
    GPIO.cleanup()
        



if __name__ == '__main__':
    main()
