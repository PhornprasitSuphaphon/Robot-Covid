import usb.core
import usb.util
import array
import time
import threading

class RFID:
    
    def __init__(self):
        self.device = usb.core.find(idVendor=0xffff, idProduct=0x35)
        self.value = None
        if self.device is None:
            raise ValueError('Device not found')
        if self.device.is_kernel_driver_active(0):
            self.device.detach_kernel_driver(0)
        self.device.set_configuration()
        self.endpoint = self.device[0][(0,0)][0]

        self.ThreadRun = threading.Thread(target=self.RUN_RFID)
        self.ThreadRun.start()

    def RUN_RFID(self):
        while (1):
            self.data = None
            self.decode = ""
            self.count = 0
            while self.count < 20:
                try:
                    self.data = self.device.read(self.endpoint.bEndpointAddress,8)
                    
                    if self.data[2] != 0:
                        self.decode += str(self.data[2])
                        self.count+=1
                        
                    else:
                        self.decode+=" "
                        self.count+=1
                            # decode += str(int(str(chr(int("0x"+str(data[2]),16))))+1)
                            # count+=1
                    
                except usb.core.USBError as e:
                    self.data = None
                    if e.args == ('Operation timed out',):
                        continue
            self.value = self.decode
            # print(self.value)
            


    def getRFID (self):    
        check_RFID = self.value
        self.value = None
        return check_RFID
    
            



