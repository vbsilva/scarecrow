import Adafruit_DHT
import RPi.GPIO as GPIO
import time
 
# Define o tipo de sensor
dht = Adafruit_DHT.DHT11
 
GPIO.setmode(GPIO.BCM)
 
# Define a GPIO conectada ao pino de dados do sensor
dht_pin = 2
 
# Informacoes iniciais
print ("*** Lendo os valores de temperatura e umidade");
 
while(1):
   # Efetua a leitura do sensor
   umid, temp = Adafruit_DHT.read_retry(dht, dht_pin);
   # Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     print("temperature: " + str(temp),)
     print("humidity: " + str(umid))
     #print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n").format(temp, umid);
     print ("Aguarda 5 segundos para efetuar nova leitura...n");
     time.sleep(5)
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")