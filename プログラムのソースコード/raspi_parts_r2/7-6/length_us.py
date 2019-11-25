import wiringpi as pi
import time
import hssr04

TRIG_PIN = 23
ECHO_PIN = 24

pi.wiringPiSetupGpio()

us_dev = hssr04.hssr04(TRIG_PIN,ECHO_PIN)

while True:
    distance = us_dev.read_distance( )

    print ("Distance:", distance, "cm" )
    time.sleep(1)
