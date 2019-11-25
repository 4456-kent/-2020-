import wiringpi as pi
import time

green_pin = 18
blue_pin = 23
red_pin = 24

pi.wiringPiSetupGpio()
pi.pinMode( green_pin, pi.OUTPUT )
pi.pinMode( blue_pin, pi.OUTPUT )
pi.pinMode( red_pin, pi.OUTPUT )

pi.softPwmCreate( green_pin, 0, 100)
pi.softPwmCreate( blue_pin, 0, 100)
pi.softPwmCreate( red_pin, 0, 100)

pi.softPwmWrite( green_pin, 0 )
pi.softPwmWrite( blue_pin, 100 )
pi.softPwmWrite( red_pin, 100 )
