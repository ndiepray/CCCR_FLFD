import paho.mqtt.client as mqtt
import json
import time
import random
import Adafruit_DHT

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect('172.30.1.5', 1883)
client.loop_start()

sensor = Adafruit_DHT.DHT11
# GPIO Number : 4
pin = 4

try:
    while(True):
        # t: temperature, h:humidity
        h, t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None :
            dict1={'temperature':t}
            dict2={'humidity':h}
        else:
            print('Read error')a
        # json file create    
        json_test1=json.dumps(dict1)
        json_test2=json.dumps(dict2)
        client.publish('temperature', json_test1, 1)
        client.publish('humidity', json_test2, 1)

except KeyboardInterrupt:
    print("Terminated by Keyboard")

finally:
    print("End of Program")

client.loop_stop()
client.disconnect()
