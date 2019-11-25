import time
import wiringpi as pi

motor1_pin = 23
motor2_pin = 24

pi.wiringPiSetupGpio()
pi.pinMode( motor1_pin, pi.OUTPUT )
pi.pinMode( motor2_pin, pi.OUTPUT )

pi.softPwmCreate( motor1_pin, 0, 100)
pi.softPwmCreate( motor2_pin, 0, 100)
pi.softPwmWrite( motor1_pin, 0 )
pi.softPwmWrite( motor2_pin, 0 )

while True:
    speed = 0
    while ( speed <= 100 ):
        pi.softPwmWrite( motor1_pin, speed )
        pi.softPwmWrite( motor2_pin, 0 )
        time.sleep(0.3)
        speed = speed + 1

    pi.softPwmWrite( motor1_pin, 100 )
    pi.softPwmWrite( motor2_pin, 100 )
    time.sleep(2)

    speed = 0
    while ( speed <= 100 ):
        pi.softPwmWrite( motor1_pin, 0 )
        pi.softPwmWrite( motor2_pin, speed )
        time.sleep(0.3)
        speed = speed + 1
        
    pi.softPwmWrite( motor1_pin, 0 )
    pi.softPwmWrite( motor2_pin, 0 )
    time.sleep(2)

