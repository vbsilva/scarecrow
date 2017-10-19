import time
import Adafruit_DHT
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import os
import sys

class Sensors(object):
    '''
        This class manages the sensors
    '''

    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.dht = Adafruit_DHT.DHT11
        GPIO.setmode(GPIO.BCM)
        self.gain = 1
        self.dht_pin = 4
        self.ldr_pin = 17
        self.relay_pin = 27
        self.blueLed_pin = 26
        self.redLed_pin = 19
        self.greenLed_pin = 13


    #     self.rain_pin = 4
    #     self.soil_pin = 18

        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.setup(self.blueLed_pin, GPIO.OUT)
        GPIO.setup(self.redLed_pin, GPIO.OUT)
        GPIO.setup(self.greenLed_pin, GPIO.OUT)

        GPIO.output(self.relay_pin, GPIO.HIGH)
        GPIO.output(self.blueLed_pin, GPIO.HIGH)
        GPIO.output(self.redLed_pin, GPIO.HIGH)
        GPIO.output(self.greenLed_pin, GPIO.HIGH)
    #     GPIO.setup(self.rain_pin, GPIO.IN)
    #     GPIO.setup(self.soil_pin, GPIO.IN)


    def __del__(self):
        pass
        #close gpios and exit program

    def blueLed(self):
        GPIO.output(self.blueLed_pin, GPIO.LOW)
        GPIO.output(self.redLed_pin, GPIO.HIGH)
        GPIO.output(self.greenLed_pin, GPIO.HIGH)

    def redLed(self):
        GPIO.output(self.redLed_pin, GPIO.LOW)
        GPIO.output(self.blueLed_pin, GPIO.HIGH)
        GPIO.output(self.greenLed_pin, GPIO.HIGH)

    def greenLed(self):
        GPIO.output(self.greenLed_pin, GPIO.LOW)
        GPIO.output(self.redLed_pin, GPIO.HIGH)
        GPIO.output(self.blueLed_pin, GPIO.HIGH)

    def noLeds(self):
        GPIO.output(self.blueLed_pin, GPIO.HIGH)
        GPIO.output(self.redLed_pin, GPIO.HIGH)
        GPIO.output(self.greenLed_pin, GPIO.HIGH)

    def get_temp_n_hum(self):
        umid, temp = Adafruit_DHT.read_retry(self.dht, self.dht_pin)

        if umid is not None and temp is not None:
            ret = []
            ret.append(temp)
            ret.append(umid)

            return ret
        else:
            print("Falha ao ler dados do DHT11 !!!")

    def get_rain(self):
        return self.adc.read_adc(1,gain=self.gain)

    def get_soil(self):
        return self.adc.read_adc(2,gain=self.gain)

    def get_lum(self):
        return self.adc.read_adc(3,gain=self.gain)

    def get_Co(self):
        return self.adc.read_adc(0,gain=self.gain)

    def set_relay(self, status):
        if status:
            GPIO.output(self.relay_pin, GPIO.LOW)
        else:
            GPIO.output(self.relay_pin, GPIO.HIGH)
