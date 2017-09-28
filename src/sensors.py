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
    #     self.rain_pin = 4
    #     self.soil_pin = 18

        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.output(self.relay_pin, GPIO.HIGH)
    #     GPIO.setup(self.rain_pin, GPIO.IN)
    #     GPIO.setup(self.soil_pin, GPIO.IN)


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
print "vai danado"

while(1):
    try:
        print "lum:",
        print test.get_lum()
        if( test.get_lum() > 3500):
             test.set_relay(True)
        else:
            test.set_relay(False)

        data = test.get_temp_n_hum()
        print "temp:",
        print data[0]
        print "hum:",
        print data[1]
        time.sleep(2)
    except KeyboardInterrupt:
        print "flw"
        GPIO.cleanup()


GPIO.cleanup()
    

