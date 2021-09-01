import time
import Adafruit_DHT

# Sensor: DH11 사용, GPIO Number : 4번
sensor = Adafruit_DHT.DHT11
pin = 4

# 1초마다 temperature data, humidity data 출력
try:
    while True :
        # t: temperature, h: humidity
        h, t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None :
            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        else :
            print('Read error')
        time.sleep(1)

except KeyboardInterrupt:
    print("Terminated by Keyboard")   

finally:
    print("End of Program")
