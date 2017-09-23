#Import des dépendances spécifiques à la fonction
from L76GPS import GNSS
from pytrack import Pytrack
from machine import Timer
import gc
import time

GPS_FIX_TIMEOUT = 30 #Duree maximale d'un essai d'acquisition de position
GPS_RETRY_INTERVAL = 60 #Duree entre deux essais d'acquisition
GPS_RETRY_TIMEOUT = (GPS_FIX_TIMEOUT+GPS_RETRY_INTERVAL)*5
#Duree maximale consecutive de tentative d'acquisition.
# Ici, on tente 5 fois une acquisition avant de passer en mode attente
GPS_TMAX_TIMEOUT = GPS_RETRY_TIMEOUT+450 #Duree entre chaque lancement du GPS, ici 15 minutes
GPS_ACTIVE=True

#Definition de la fonction
def gpsThread():
	global GPS_ACTIVE
	GPS_ACTIVE = True
	py=Pytrack()
	gps=GNSS(py, timeout = GPS_FIX_TIMEOUT)
	chronoTMAX=Timer.Chrono()
	chronoRETRY=Timer.Chrono()

	chronoTMAX.start()
	coord = gps.coordinates()
	chronoRETRY.start()
	while (chronoRETRY.read() < GPS_RETRY_TIMEOUT):
		if (coord !=(None, None, None)):
			#ecriture_fichier_positions()
			if (chronoTMAX.read() >= GPS_TMAX_TIMEOUT):
				gc.collect()
				GPS_ACTIVE=False
				return
			else:
				time.sleep(GPS_TMAX_TIMEOUT-chronoTMAX.read())
				gc.collect()
				GPS_ACTIVE=False
				return
		else:
			time.sleep(GPS_RETRY_INTERVAL)
	gc.collect()
	GPS_ACTIVE = False
