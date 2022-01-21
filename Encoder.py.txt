import threading
from time import sleep
class Encoder:

    def __init__(self,gpio,pin_A,count_round):
        self.Count_Round = count_round #??????Encoder1???
        self._Degree=int(self.Count_Round/360)
        self.Count_Degree = 0
        self._Out_Degree = 0;
        self.GPIO = gpio     
        self.PIN_A = pin_A
        self.PIN_B = True
        self.GPIO.setup(self.PIN_A, self.GPIO.IN) 
        self.NowState =0
        self.Lasttate =0
        self._Counter = 0
        self.countDistance  = 0
        self.Distance =0
        self.ThreadRun = threading.Thread(target=self.do_Encoder)
        self.ThreadRun.start()
        sleep(0.001)


    def do_Encoder(self):
        while True:
            self.NowState = self.GPIO.input(self.PIN_A)
            if self.Lasttate != self.NowState  :
                if self.PIN_B :
                    self._Counter+=1
                    self.Count_Degree+=1
                    if self.Count_Degree == self._Degree :
                        self._Out_Degree+=1
                        Count_Degree =0
                else:
                    self._Counter-=1
                    self.Count_Degree-=1
                    if self.Count_Degree == (-self._Degree) :
                        self._Out_Degree+=1
                        Count_Degree =0
                
                    
            self.Lasttate = self.NowState

            
    def setDT(self,dt):
        self.PIN_B = dt
    def get(self):
        return self._Counter
    def getDegree(self,degree):
        self.Degree = degree
        self.result = (self.Count_Round/360)*self.Degree
        return self.result
    
    def getDistance(self):
        self.r = 6 #cm
        self.circumference  = (2*3.14)*self.r
        self.Distance = (self.Count_Round/self.circumference)
       
        if self.Counter >= self.Distance:
            self.countDistance +=1
            reset()
            
        return self.countDistance 
    
    def reset(self):
        self.Counter = 0
