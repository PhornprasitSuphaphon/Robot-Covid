from time import sleep
import RPi.GPIO as GPIO  
from Encoder import Encoder
from motor import motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT) 
GPIO.output(27,GPIO.HIGH)
# Encoder_B = Encoder(GPIO,5,10000)
# Encoder_C = Encoder(GPIO,6,30000)
# motor_B = motor(GPIO,17,27,13,Encoder_B)
# motor_B.stop()
sleep(1)
# GPIO.setup(5, GPIO.IN) 
# GPIO.setup(6, GPIO.IN)
while True:
        # motor_B.Forward(100)
        print(Encoder_B._Counter)
        