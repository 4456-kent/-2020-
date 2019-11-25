import wiringpi as pi
import hsv_to_rgb
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

while True:
    hue = 0
    while ( hue < 1 ):
        ( red, green, blue ) = hsv_to_rgb.hsv_to_rgb( hue, 1.0, 1.0 )

        pi.softPwmWrite( green_pin, int( green * 100 ) )
        pi.softPwmWrite( blue_pin, int( blue * 100 ) )
        pi.softPwmWrite( red_pin, int( red * 100 ) )

        hue = hue + 0.01

        time.sleep(0.1)





