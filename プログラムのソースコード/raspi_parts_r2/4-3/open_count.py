import wiringpi as pi
import time

SW_PIN = 4

pi.wiringPiSetupGpio()
pi.pinMode( SW_PIN, pi.INPUT )
pi.pullUpDnControl( SW_PIN, pi.PUD_DOWN )

count = 0

while True:
    if ( pi.digitalRead( SW_PIN ) == pi.HIGH ):
        time.sleep( 0.1 )
        
        count = count + 1
        print ("Count : " , count )

        while ( pi.digitalRead( SW_PIN ) == pi.HIGH ):
            time.sleep( 0.1 )

        time.sleep( 0.1 )
