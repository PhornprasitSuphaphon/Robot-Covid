import serial
import threading
from time import sleep
class LightSensor :

    def __init__(self,port_USB,baudrate,gpio,pinreset): 
        self.GPIO= gpio
        self.PinReset = pinreset
        self.GPIO.setup(self.PinReset, self.GPIO.OUT) 
        self.GPIO.output(self.PinReset,self.GPIO.LOW)
        sleep(0.1)
        self.GPIO.output(self.PinReset,self.GPIO.HIGH)
        self.port = serial.Serial(port_USB,baudrate,timeout=0.5)
        self.ThreadRun = threading.Thread(target=self.do_Encoder)
        self.ThreadRun.start()
        self.msg=0
    def do_Encoder(self):
        while True:
            try:
                # self.msg = self.port.readline().decode('utf-8').rstrip())
                self.msg =int(self.port.readline().decode('utf-8').rstrip());
                #self.port.flushInput()
            except ValueError:
                self.msg=0

    def get(self):
        Send = self.msg
        self.msg=0
        return Send

        