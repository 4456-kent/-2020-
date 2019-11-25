import wiringpi as pi

DISP_NUMBER = 5
DISP_DP = 0

BIT_PIN = [ 14, 15, 23, 24 ]
DP_PIN = 25

pi.wiringPiSetupGpio()
for pin in BIT_PIN:
    pi.pinMode( pin, pi.OUTPUT )
pi.pinMode( DP_PIN, pi.OUTPUT )

i = 0
while ( i < 4 ):
    pi.digitalWrite( BIT_PIN[i], DISP_NUMBER & ( 0x01 << i ) )
    i = i + 1

pi.digitalWrite( DP_PIN, DISP_DP )
