import gps
import serial
import time

BAUD_RATE=9600  #ボーレート9600bps
TIMEOUT=1   #タイムアウト1[s]
DISTANCE_LAT=35.6185408
DISTANCE_LNG=139.3850305

g=gps.gps(BAUD_RATE,TIMEOUT,DISTANCE_LAT,DISTANCE_LNG)

while True:
    print('%f[m]\n'%g.distance_cal())
    print('%f[deg]\n'%g.direction_cal())
    time.sleep(1)

