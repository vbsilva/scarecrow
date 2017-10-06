import os
import time
import cv2
import numpy as np
import sensors
import imgprocessing
import sconn

'''
    This is the main Module of the program
'''

def packdata(data):
    

def send_message(data,sigfox)
    data = packdata(data)
    sigfox.send_message(data)

def main():
    '''
        Main Function of the program
    '''
    print("Scarecrow starting...")
    print("Loading Sensors")
    source = Sensors()
    sigfox = SerialConnection() 
    time.sleep(0.1)
    print("Loading AIModel")
    img_handler = ImgProcessing(camera=1,debug=True)
    print("AI Model loaded")
    while(True):
        try:
            data = source.get_temp_n_hum()
            temperature = data[0]
            humidity = data[1]
            luminosity = source.get_lum()
            rain = source.get_rain()
            soil = source.get_soil()
            bugs = img_handle.process_image()
            data = [bugs,soil,rain,luminosity,humidity,temperature]
            send_message(data)
        except KeyboardInterrupt:
            print("flw")
            GPIO.cleanup()
    
        time.sleep(10)
    
    GPIO.cleanup()
        



if __name__ == '__main__':
    main()
