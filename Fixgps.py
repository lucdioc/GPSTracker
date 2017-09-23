#Dépendances
#from connectWifi import connectWifi
#from L76GNSS2 import L76GNSS2
#from pytrack import Pytrack

#Se connecte à un réseau Wifi
#connectWifi()

#Initialise les objets
py = Pytrack()
l76 = L76GNSS2(py, timeout=30)

while (True):
    coord = l76.coordinates(True)
    print("{}".format(coord))
