import time
import wiringpi as pi

motor_pin = 23

pi.wiringPiSetupGpio()
pi.pinMode( motor_pin, pi.OUTPUT )

while True:
    pi.digitalWrite( motor_pin, pi.HIGH )
    time.sleep( 2 )

    pi.digitalWrite( motor_pin, pi.LOW )
    time.sleep( 2 )
