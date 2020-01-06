import gps
import serial

BAUD_RATE=9600  #ボーレート9600bps
TIMEOUT=1   #タイムアウト1[s]
DISTANCE_LAT=35.6185408
DISTANCE_LNG=139.3850305

g=gps.gps(BAUD_RATE,TIMEOUT)

g.setup()

print(g.gprmc())

