import wiringpi as pi

INPUT_PIN = 24

pi.wiringPiSetupGpio()
pi.pinMode( INPUT_PIN, pi.INPUT )

value = pi.digitalRead( INPUT_PIN )

print( value )
