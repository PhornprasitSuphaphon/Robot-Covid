from time import sleep
class motor:
    def __init__(self,gpio): 
        self.GPIO = gpio     
        print("You have not set GPIO motor")
   
    def __init__(self,gpio,pin_A,pin_B,pin_pwm):
        self.GPIO = gpio
        self._PIN_A = pin_A
        self._PIN_B = pin_B
        self._PIN_PWM = pin_pwm
        self.GPIO.setup(self._PIN_A, self.GPIO.OUT) 
        self.GPIO.setup(self._PIN_B, self.GPIO.OUT)
        self.GPIO.setup(self._PIN_PWM, self.GPIO.OUT)
        self.OUT_PWM = self.GPIO.PWM(self._PIN_PWM, 100) 
        self.OUT_PWM.start(0)

    def Forward(self,Speed):
        self._Speed = Speed
        if self._Speed>100:
            self._Speed =100
        if self._Speed<0:
            self._Speed =0
        self.OUT_PWM.ChangeDutyCycle(self._Speed)       
        self.GPIO.output(self._PIN_A,self.GPIO.HIGH)
        self.GPIO.output(self._PIN_B,self.GPIO.LOW)

    def BackForward(self,Speed):
        self._Speed = Speed
        if self._Speed>100:
            self._Speed =100
        if self._Speed<0:
            self._Speed =0
        self.OUT_PWM.ChangeDutyCycle(self._Speed)       
        self.GPIO.output(self._PIN_A,self.GPIO.LOW)
        self.GPIO.output(self._PIN_B,self.GPIO.HIGH)

   

    def ON(self,Speed): 
        self._Speed = Speed
        if self._Speed>100:
            self._Speed =100
        
        if self._Speed<-100:
            self._Speed =-100
        if self._Speed >0 : 
            self.OUT_PWM.ChangeDutyCycle(self._Speed)       
            self.GPIO.output(self._PIN_A,self.GPIO.HIGH)
            self.GPIO.output(self._PIN_B,self.GPIO.LOW)
        elif self._Speed <0:
            self.OUT_PWM.ChangeDutyCycle(abs(self._Speed)) 
            self.GPIO.output(self._PIN_A,self.GPIO.LOW)
            self.GPIO.output(self._PIN_B,self.GPIO.HIGH)
        else :
            self.GPIO.output(self._PIN_A,self.GPIO.LOW)
            self.GPIO.output(self._PIN_B,self.GPIO.LOW)
    def OFF (self): 
        self.OUT_PWM.ChangeDutyCycle(0) 
        self.GPIO.output(self._PIN_A,self.GPIO.LOW)
        self.GPIO.output(self._PIN_B,self.GPIO.LOW)
        