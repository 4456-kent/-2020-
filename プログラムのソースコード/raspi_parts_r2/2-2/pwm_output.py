import wiringpi as pi

OUTPUT_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode( OUTPUT_PIN, pi.OUTPUT )

pi.softPwmCreate( OUTPUT_PIN, 0, 100)

pi.softPwmWrite( OUTPUT_PIN, 50 )
