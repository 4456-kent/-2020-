import wiringpi as pi
import time

SW_PIN = 4

pi.wiringPiSetupGpio()
pi.pinMode( SW_PIN, pi.INPUT )

while True:
    if ( pi.digitalRead( SW_PIN ) == pi.HIGH ):
        print ("Switch is ON")
    else:
        print ("Switch is OFF")

    time.sleep( 1 )
