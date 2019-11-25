import time
import wiringpi as pi

motor1_pin = 23
motor2_pin = 24

pi.wiringPiSetupGpio()
pi.pinMode( motor1_pin, pi.OUTPUT )
pi.pinMode( motor2_pin, pi.OUTPUT )

while True:
    pi.digitalWrite( motor1_pin, pi.HIGH )
    pi.digitalWrite( motor2_pin, pi.LOW )

    time.sleep(2)

    pi.digitalWrite( motor1_pin, pi.HIGH )
    pi.digitalWrite( motor2_pin, pi.HIGH )
    time.sleep(2)
    
    pi.digitalWrite( motor1_pin, pi.LOW )
    pi.digitalWrite( motor2_pin, pi.HIGH )
    time.sleep(2)

    pi.digitalWrite( motor1_pin, pi.LOW )
    pi.digitalWrite( motor2_pin, pi.LOW )
    time.sleep(2)
    
