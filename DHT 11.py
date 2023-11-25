#pip install thingspeak 

import thingspeak 

import time 

from grovepi import * 

  

dht_sensor_port = 7 

dht_sensor_type = 0 

  

channel_id = '708030' # PUT CHANNEL ID HERE 

write_key  = 'ISN7XMLHUY9C137Q' # PUT YOUR WRITE KEY HERE 

  

def measure(channel): 

  try: 

    [ t,h ] = dht(dht_sensor_port,dht_sensor_type) 

    response = channel.update({'field1': t, 'field2': h}) 

    print("Temp:{t} C Humidity:{h}%") 

  except: 

    print("connection failed") 