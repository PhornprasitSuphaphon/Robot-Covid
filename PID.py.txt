class PID:
    def __init__(self,setpoint,kp,kd):
        self.error = 0
        self.old_error = 0
        self.PD =0
        self._kp = kp
        self._kd = kd
        self._setpoint = setpoint
        self.Max_Speed =  100
        self.Min_Speed = -100
        self.motor_speed =0
        self._setpoint = setpoint

    def set (self,setpoint,Kp,Kd):
        self._setpoint = setpoint
        self._kp = Kp 
        self._kd = Kd


    def controller (self,input):
        self._type = type
        self._input = input
        self.old_error =  self.error
        self.error = self._input - self._setpoint

        self.PD  = (self.error*self._kp+(self.old_error-self.error)*self._kd)


        self.motor_speed = self.PD

        if self.motor_speed >= self.Max_Speed:
            self.motor_speed = self.Max_Speed

        if self.motor_speed <= self.Min_Speed:
            self.motor_speed = self.Min_Speed   

    def getOutput (self):
        return self.motor_speed
    
    def getError (self):
        return self.error
    

