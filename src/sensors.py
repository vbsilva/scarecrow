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
        self.dht_pin = 25
        self.relay_pin = 27
        self.blueLed_pin = 21
        self.redLed_pin = 16
        self.greenLed_pin = 20



        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.setup(self.blueLed_pin, GPIO.OUT)
        GPIO.setup(self.redLed_pin, GPIO.OUT)
        GPIO.setup(self.greenLed_pin, GPIO.OUT)

        GPIO.output(self.relay_pin, GPIO.HIGH)
        GPIO.output(self.blueLed_pin, GPIO.HIGH)
        GPIO.output(self.redLed_pin, GPIO.HIGH)
        GPIO.output(self.greenLed_pin, GPIO.HIGH)

        self.redLed()


    def __del__(self):
        print("destructor")
        GPIO.cleanup()
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

    def blinkRed(self):
        GPIO.output(self.redLed_pin, GPIO.LOW)
        GPIO.output(self.blueLed_pin, GPIO.HIGH)
        GPIO.output(self.greenLed_pin, GPIO.HIGH)

        time.sleep(0.1)
        GPIO.output(self.redLed_pin, GPIO.HIGH)

        time.sleep(0.1)
        GPIO.output(self.redLed_pin, GPIO.LOW)

        time.sleep(0.1)
        GPIO.output(self.redLed_pin, GPIO.HIGH)

        time.sleep(0.1)
        GPIO.output(self.redLed_pin, GPIO.LOW)

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
        return self.adc.read_adc(0,gain=self.gain)

    def get_soil(self):
        return self.adc.read_adc(1,gain=self.gain)

    def get_lum1(self):
        return self.adc.read_adc(2,gain=self.gain)

    def get_lum2(self):
        return self.adc.read_adc(3,gain=self.gain)

    def set_relay(self, status):
        if status:
            GPIO.output(self.relay_pin, GPIO.LOW)
        else:
            GPIO.output(self.relay_pin, GPIO.HIGH)


source = Sensors()

while(True):
    print("lendo...")
    data = source.get_temp_n_hum()
    temperature = data[0]
    humidity = data[1]
    print (data)
    luminosity1 = source.get_lum1()
    print("Raw Lum1 :",luminosity1)
    if luminosity1 >= 20000:
        luminosity1 = 0
    elif luminosity1 >= 10000:
        luminosity1 = 1
    elif luminosity1 >= 5000:
        luminosity1 = 2
    else:
        luminosity1 = 3

    luminosity2 = source.get_lum2()
    print("Raw Lum2 :",luminosity2)
    if luminosity2 >= 20000:
        luminosity2 = 0
    elif luminosity2 >= 10000:
        luminosity2 = 1
    elif luminosity2 >= 5000:
        luminosity2 = 2
    else:
        luminosity2 = 3

    rain = source.get_rain()
    print("Raw Rain :",rain)
    if rain >= 5000:
        rain = 1
    else:
        rain = 0
    soil = source.get_soil()
    print("Raw Soil Hum :",soil)
    if soil >= 20000:
        soil = 0
    elif soil > 12000:
        soil = 1
    else:
        soil = 2
    '''if luminosity <= 1:
        source.set_relay(True)
    else:
        source.set_relay(False)
    data = [luminosity,0,rain,soil]
    print(data)'''
    x = input()
    if x == 'r':
        print("red")
        source.redLed()
        source.set_relay(True)
    elif x == 'g':
        print("green")
        source.greenLed()
        source.set_relay(False)

    elif x == 'b':
        print("blue")
        source.blueLed()
    else:
        print("else")
        source.blinkRed()