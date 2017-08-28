import Adafruit_DHT
import RPi.GPIO as GPIO
import time
 
dht = Adafruit_DHT.DHT11
 
GPIO.setmode(GPIO.BCM)
 
dht_pin = 2
ldr_pin = 3

def rc_time(ldr_pin):
  count = 0

  GPIO.setup(ldr_pin, GPIO.OUT)
  GPIO.output(ldr_pin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(ldr_pin, GPIO.IN)

  while(GPIO.input(ldr_pin) == GPIO.LOW):
    count += 1

  return count
 
 
while(1):

  print (rc_time(ldr_pin))

  umid, temp = Adafruit_DHT.read_retry(dht, dht_pin);
  if umid is not None and temp is not None:
    print("temperature: " + str(temp),)
    print("humidity: " + str(umid))
    print ("Aguarda 5 segundos para efetuar nova leitura...");
    time.sleep(2)
  else:
    print("Falha ao ler dados do DHT11 !!!")