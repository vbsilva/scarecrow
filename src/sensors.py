import time
import Adafruit_DHT
import RPi.GPIO as GPIO

class Sensors(object):
    '''
        This calss manages the sensors
    '''

    def __init__(self):
        self.dht_pin = 2
        self.ldr_pin = 3
        self.rain_pin = 4
        self.soil_pin = 14

    def rc_time(self):
        count = 0
        GPIO.setup(self.ldr_pin, GPIO.OUT)
        GPIO.outout(self.ldr_pin, GPIO.LOW)
        time.sleep(0.1)

        while GPIO.input(self.ldr_pin) == GPIO.LOW:
            count += 1

        return count
