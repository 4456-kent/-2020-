import time, wiringpi as pi

class hssr04:
    def __init__( self, trig, echo ):
        self.trig_pin = trig
        self.echo_pin = echo
        pi.pinMode( self.trig_pin, pi.OUTPUT )
        pi.pinMode( self.echo_pin, pi.INPUT )
        pi.digitalWrite( self.trig_pin, pi.LOW )
        time.sleep(0.1)

    def read_distance( self ):
        pi.digitalWrite( self.trig_pin, pi.HIGH )
        time.sleep(0.00001)
        pi.digitalWrite( self.trig_pin, pi.LOW )
        while ( pi.digitalRead( self.echo_pin ) == pi.LOW ):
            sigoff = time.time()
        while ( pi.digitalRead( self.echo_pin ) == 1 ):
            sigon = time.time()
        return ( sigon - sigoff ) * 17000





