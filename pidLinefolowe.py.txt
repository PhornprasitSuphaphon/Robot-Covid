from motor import motor
from LightSensor import LightSensor
from PID import PID
from time import sleep
import RPi.GPIO as GPIO  
from Encoder import Encoder 
from RFID import RFID
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO.setup(22,GPIO.OUT)
# GPIO.output(22,GPIO.HIGH)
# sleep(0.5)
# GPIO.output(22,GPIO.LOW)
setpoin = -7
kp = 0.7
kd = 0.2
motor_left = motor(GPIO,17,27,13)
motor_right = motor(GPIO,16,26,12)
# Encoder_C = Encoder(GPIO,5,6)
# Encoder_B = Encoder(GPIO,24,23)
sensor = LightSensor("/dev/ttyUSB0",115200,GPIO,22)
isOne = False
PID1 =None

Rfid = RFID()

motor_left.OFF()   
motor_right.OFF()
sleep(1)
while True:
    p = sensor.get()
    if Rfid.getRFID()!= None:
        print("aa")
    if p != 0:
        if isOne == False:
            PID1 = PID(setpoin,kp,kd)
            isOne = True
        else:
            if p ==0:
                motor_left.stop()   
                motor_right.stop()
            else:
                    if abs(p) < 330:
                        PID1.controller(p) 
                        
                        motor_left.ON(60-(PID1.getOutput()*0.9))    
                        motor_right.ON(100+(PID1.getOutput()))  
                        print("output :"+str(p) + " Output: " +str(PID1.getOutput()))
                            #print("output :"+str(p))
                    else:
                        motor_left.OFF()   
                        motor_right.OFF()
# while True:
#         if abs(Encoder_C.get()) < 2000 :
#             motor_B.on(50)    
        #motor_C.on(85) 
            #print(" Encoder_C : " + str(abs(Encoder_C.get()))+ " Encoder_B : " + str(abs(Encoder_B.get())))
  
