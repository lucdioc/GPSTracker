#Dependances
import machine
import json
from network import LoRa
import socket
import binascii
import struct
import time

#Configuration
with open("/flash/conf/loraAppID.json") as json_data_file:
    appIDTupple=json.load(json_data_file)

#Définition de la fonction
def lora3TelecomJoin()

	# Initialize LoRa in LORAWAN mode.
	lora = LoRa(mode=LoRa.LORAWAN)

	# create an OTAA authentication parameters
	app_eui = binascii.unhexlify('BE 7B 00 00 00 00 00 99'.replace(' ',''))
	app_key = binascii.unhexlify('BE 5A 4D 2F 1E 01 26 6D 38 0D E3 1C 04 52 24 4F'.replace(' ',''))

	# join a network using OTAA (Over the Air Activation)
	lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

	# wait until the module has joined the network
	while not lora.has_joined():
    		time.sleep(2.5)
    		print('Not yet joined...')

	# create a LoRa socket
	s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

	# set the LoRaWAN data rate
	s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
	s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, True)

	# make the socket blocking
	# (waits for the data to be sent and for the 2 receive windows to expire)
	s.setblocking(True)

	# send some data
	s.send(bytes([0x01, 0x02, 0x03]))

	# make the socket non-blocking
	# (because if there's no data received it will block forever...)
	s.setblocking(False)

	# get any data received (if any...)
	data = s.recv(64)
	print(data)
