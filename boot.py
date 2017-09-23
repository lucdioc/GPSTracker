#Dependances
import os
import machine
from machine import UART
from connectWifi import connectWifi

uart = UART(0, 115200)
os.dupterm(uart)

#Se connecte � un r�seau Wifi
connectWifi()

#Lance le processus principal
machine.main('accel.py')
