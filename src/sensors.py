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

test = Sensors()
print ("\t\tSCARECROW")
time.sleep(0.1)

while(1):
    try:
        print("\n\n\n\nReadings : \n\n")
       # if( test.get_lum() > 4000):
       #      test.set_relay(True)
       #      test.redLed()
       # else:
       #     test.set_relay(False)
       #     test.greenLed()
        luminosity = test.get_lum()
        print("Luminosity = ",luminosity)
        if luminosity >= 20000:
           luminosity = 0
        elif luminosity >= 10000:
           luminosity = 1
        elif luminosity >= 5000:
           luminosity = 2
        elif luminosity < 5000:
           luminosity = 3
        temp,hum = test.get_temp_n_hum()
        rain = test.get_rain()
        soilhum = test.get_soil()
        print("Temperature : ", temp)
        print("Humidity : ", hum)
        print("Water : ", test.get_rain())
        print("Soil Humidity: ",test.get_soil())
        if rain >= 5000:
           rain = 1
        else:
           rain = 0
        if soilhum >= 20000:
           soilhum = 0
        else:
           soilhum = 1
        print("L, Temp, Hum, Rain, SoilHum")
        data = [int(luminosity),int(temp),int(hum),int(rain),int(soilhum)]
        print(data)
        #print("Co2: ", test.get_Co())
        test.blueLed()
        time.sleep(2)
        test.redLed()
        time.sleep(2)
        test.greenLed()
        time.sleep(2)
        test.noLeds()
    except KeyboardInterrupt:
        print ("flw")
        GPIO.cleanup()

    time.sleep(2)



GPIO.cleanup()
    

