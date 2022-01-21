from LightSensor import LightSensor
import RPi.GPIO as GPIO   
import time
error = 0
GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)

sensor= LightSensor("/dev/ttyUSB0",115200)
while 1 :
    a = sensor.get()
    if a!=0 :
        print(a)


