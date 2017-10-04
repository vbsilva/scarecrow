import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import os

class Sensors(object):
    '''
        This class manages the sensors
    '''

    def __init__(self):
        self.dht = Adafruit_DHT.DHT11
        GPIO.setmode(GPIO.BCM)

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

    # def get_rain(self):
    #     return GPIO.input(self.rain_pin)

    # def get_soil(self):
    #     return GPIO.input(self.soil_pin)

    def get_lum(self):
        count = 0
        GPIO.setup(self.ldr_pin, GPIO.OUT)
        GPIO.output(self.ldr_pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(self.ldr_pin, GPIO.IN)
        while GPIO.input(self.ldr_pin) == GPIO.LOW:
            count += 1

        return count

    def set_relay(self, status):
        if status:
            GPIO.output(self.relay_pin, GPIO.LOW)
        else:
            GPIO.output(self.relay_pin, GPIO.HIGH)


test = Sensors()
print "\t\tSCARECROW"
time.sleep(0.1)

while(1):
    try:
        print "lum:",
        print test.get_lum()
        if( test.get_lum() > 4000):
             test.set_relay(True)
             test.redLed()
        else:
            test.set_relay(False)
            test.greenLed()

        data = test.get_temp_n_hum()
        print "temp:",
        print data[0]
        print "hum:",
        print data[1]
        test.blueLed()
    except KeyboardInterrupt:
        print "flw"
        GPIO.cleanup()

    time.sleep(2)



GPIO.cleanup()
    

