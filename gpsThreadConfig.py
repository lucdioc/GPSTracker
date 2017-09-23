GPS_FIX_TIMEOUT = 30 #Duree maximale d'un essai d'acquisition de position
GPS_RETRY_INTERVAL = 60 #Duree entre deux essais d'acquisition
GPS_RETRY_TIMEOUT = (GPS_FIX_TIMEOUT+GPS_RETRY_INTERVAL)*5
#Duree maximale consecutive de tentative d'acquisition.
# Ici, on tente 5 fois une acquisition avant de passer en mode attente
GPS_TMAX_TIMEOUT = GPS_RETRY_TIMEOUT+450 #Duree entre chaque lancement du GPS, ici 15 minutes
GPS_ACTIVE=True
