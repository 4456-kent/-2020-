import wiringpi as pi

DISP_NUMBER = 5
DISP_DP = 0

SEG_PIN = [ 6, 12, 13, 19, 16, 26, 20 ]
DP_PIN = 21

SEG_SHAPE = [ 0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f ]

pi.wiringPiSetupGpio()
for pin in SEG_PIN:
    pi.pinMode( pin, pi.OUTPUT )
pi.pinMode( DP_PIN, pi.OUTPUT )

shape = SEG_SHAPE[DISP_NUMBER]
pi.digitalWrite( SEG_PIN[0], shape & 0x01 )
pi.digitalWrite( SEG_PIN[1], shape & 0x02 )
pi.digitalWrite( SEG_PIN[2], shape & 0x04 )
pi.digitalWrite( SEG_PIN[3], shape & 0x08 )
pi.digitalWrite( SEG_PIN[4], shape & 0x10 )
pi.digitalWrite( SEG_PIN[5], shape & 0x20 )
pi.digitalWrite( SEG_PIN[6], shape & 0x80 )
pi.digitalWrite( DP_PIN, DISP_DP )
