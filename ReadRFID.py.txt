import RPi.GPIO as GPIO
from Encoder import Encoder
from motor import motor
from LightSensor import LightSensor
from PID import PID
from time import sleep
from TcpClient import TcpClient
from RFID import RFID
import simplejson as json


_RFID = RFID()



while 1:
    check_RFID = _RFID.getRFID()
    if check_RFID!=None:
        print("Scan :"+check_RFID)

    