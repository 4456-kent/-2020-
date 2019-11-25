import wiringpi as pi
from so1602 import so1602

so1602_addr = 0x3c

i2c = pi.I2C()
so1602 = so1602( i2c, so1602_addr )

so1602.move_home( i2c )
so1602.set_cursol( i2c, 0 )
so1602.set_blink( i2c, 0 )

so1602.clear(i2c)
so1602.move( i2c, 0, 0 )
so1602.write( i2c, "Let's Enjoy" )
so1602.move( i2c, 2, 1 )
so1602.write( i2c, "Raspberry Pi !" )
