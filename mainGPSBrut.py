import machine
import math
import network
import os
import time
import utime
from machine import RTC #remote time control : gestion du temps et de l'horodatage
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS
from pytrack import Pytrack
# setup as a station

import gc #garbage collector

time.sleep(2)
gc.enable()

# configuration de l'horodatage
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
chrono = Timer.Chrono()
chrono.start()


#sd = SD()
#os.mount(sd, '/sd')
#f = open('/sd/gps-record.txt', 'w')
while (True):

    coord = l76.coordinates()
    #f.write("{} - {}\n".format(coord, rtc.now()))
    print("{} - {} - {}".format(coord, rtc.now(), gc.mem_free()))
