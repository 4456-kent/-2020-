import time, wiringpi as pi
import time

class gp2y0e03:
    def __init__( self, i2c, ad ):
        self.ad = ad
        self.i2c = i2c
        self.device = i2c.setup( ad )
        time.sleep(1)

    def read_distance( self ):
        shift = self.i2c.readReg8( self.device, 0x35 )
        d_h = self.i2c.readReg8( self.device, 0x5e )
        d_l = self.i2c.readReg8( self.device, 0x5f )

        d = ( d_h << 4 ) + d_l
        distance = d / ( 16 * pow( 2, shift ) )

        return( distance )
