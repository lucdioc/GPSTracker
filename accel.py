from gpsThread import gpsThread
import math
import _thread

def isMoving(seuilMouv=0.1, intervalle=1):
    lectureAccel=LIS2HH12()
    acceln=lectureAccel.acceleration()[0:2]
    time.sleep(intervalle)
    acceln1=lectureAccel.acceleration()[0:2]
    if math.sqrt(math.pow(acceln[0]-acceln1[0],2)+math.pow(acceln[1]-acceln1[1],2))<seuilMouv:
        return False
    else:
        return True

def principale(tempsSommeil = 10000, seuilMouv=0.1,intervalleMouv=1):
    while True:
        if not isMoving(seuilMouv,intervalleMouv):
            machine.deepsleep(tempsSommeil)
        else:
            print('coucou')
            _thread.start_new_thread(gpsThread())

principale()
