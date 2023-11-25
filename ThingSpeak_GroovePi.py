from grovepi import *
import sys
import os
import time
import urllib
from urllib import request

myAPI = "UQ23MHIAUDICFIF8"  # API Key from thingSpeak.com channel
myDelay = 15 #how many seconds between posting data

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger = 4
Relay_pin = 2

pinMode(Relay_pin,"OUTPUT")

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while True:
    try:
           # Read distance value from Ultrasonic
            distant = 5#ultrasonicRead(ultrasonic_ranger)
            time.sleep(0.5)
                        
            distant=str(distant)
            f = urllib.request.urlopen(baseURL + "&field1=%s" %distant)
            f.close()

            print(distant)

            time.sleep(int(myDelay))

        

    except TypeError:
        print("Error")
    except IOError:
        print("Error")
