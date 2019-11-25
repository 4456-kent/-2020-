import wiringpi as pi
import time

PIR_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode( PIR_PIN, pi.INPUT )

while True:
    if ( pi.digitalRead( PIR_PIN ) == pi.HIGH ):
        print ("IR ON.")
    else:
        print ("IR OFF.")

    time.sleep( 1 )
