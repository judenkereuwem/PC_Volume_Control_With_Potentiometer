#This project helps you control the volume on your PC with Arduino-potentiometer 

import pyautogui
import serial
import time
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


ser = serial.Serial('COM5', 9600)
time.sleep(2)

while True:
    b = ser.readline()
    signal = b.decode('latin-1')
    #print("pot: ",signal)

    vol = np.interp(signal, [0,100],[-65, 0])
    volume.SetMasterVolumeLevel(vol, None)

    signal = "";

ser.close()
