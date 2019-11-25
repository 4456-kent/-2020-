import wiringpi as pi

SEG_PIN = [ 6, 12, 13, 19, 16, 26, 20 ]
DP_PIN = 21

pi.wiringPiSetupGpio()
for pin in SEG_PIN:
    pi.pinMode( pin, pi.OUTPUT )
pi.pinMode( DP_PIN, pi.OUTPUT )

pi.digitalWrite( SEG_PIN[0], pi.HIGH )
pi.digitalWrite( SEG_PIN[1], pi.HIGH )
pi.digitalWrite( SEG_PIN[2], pi.LOW )
pi.digitalWrite( SEG_PIN[3], pi.HIGH )
pi.digitalWrite( SEG_PIN[4], pi.HIGH )
pi.digitalWrite( SEG_PIN[5], pi.LOW )
pi.digitalWrite( SEG_PIN[6], pi.HIGH )
pi.digitalWrite( DP_PIN, pi.LOW )
