import time, wiringpi as pi

HT16K33_ADDR = 0x70

output = [ 0b00111100,
           0b01000010,
           0b10100101,
           0b10000001,
           0b10100101,
           0b10011001,
           0b01000010,
           0b00111100 ]

matrix_row = 8
matrix_col = 8

pi.wiringPiSetupGpio()
i2c = pi.I2C()

ht16k33 = i2c.setup( HT16K33_ADDR )
i2c.writeReg8( ht16k33, 0x21, 0x01 )
i2c.writeReg8( ht16k33, 0x81, 0x01 )

time.sleep(0.1)

row = 0
while ( row < matrix_row ):
    i2c.writeReg8( ht16k33, row * 2, output[row] )
    row = row + 1
