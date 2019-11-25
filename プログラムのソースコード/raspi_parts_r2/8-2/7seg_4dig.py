import time, wiringpi as pi

DISP_NUMBER = [ 1, 2, 3, 4 ]
DISP_DP = [ 0, 0, 0, 0 ]
BIT_PIN = [ 14, 15, 23, 24 ]
DIG_PIN = [ 21, 20, 16, 12 ]

DP_PIN = 25

DIG = 4
WAIT_TIME = 0.05

pi.wiringPiSetupGpio()
for pin in BIT_PIN:
    pi.pinMode( pin, pi.OUTPUT )
for pin in DIG_PIN:
    pi.pinMode( pin, pi.OUTPUT )
    pi.digitalWrite( pin, pi.HIGH )
    pi.pinMode( DP_PIN, pi.OUTPUT )

while True:
    dig = 0
    while ( dig < DIG ):
        i = 0
        while ( i < 4 ):
            pi.digitalWrite( BIT_PIN[i], DISP_NUMBER[dig] & ( 0x01 << i ) )
            i = i + 1

        pi.digitalWrite( DP_PIN, DISP_DP[dig] )
        pi.digitalWrite( DIG_PIN[dig], pi.LOW )
        
        time.sleep( WAIT_TIME )
        pi.digitalWrite( DIG_PIN[dig], pi.HIGH )
        dig = dig + 1
