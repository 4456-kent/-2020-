import time, wiringpi as pi
import dig_sprit

number = 1234
HT16K33_ADDR = 0x70
DIGIT = 4 

SEG_CHAR = [ 0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x67 ]

DISP_NUMBER = [ 0, 0, 0, 0 ]
DISP_NUMBER = dig_sprit.dig_sprit( number, DIGIT )

i2c = pi.I2C()

ht16k33 = i2c.setup( HT16K33_ADDR )
i2c.writeReg8( ht16k33, 0x21, 0x01 )
i2c.writeReg8( ht16k33, 0x81, 0x01 )

time.sleep(0.1)

i = 0
while (i < DIGIT ):
    i2c.writeReg8( ht16k33, i * 2, SEG_CHAR[ DISP_NUMBER[i] ] )
    i = i + 1
