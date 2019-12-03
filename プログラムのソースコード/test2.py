import wiringpi as pi
import time

OUTPUT_PIN=23

pi.wiringPiSetupGpio()
pi.pinMode(OUTPUT_PIN,pi.OUTPUT)


while True:
    pi.digitalWrite(OUTPUT_PIN,pi.LOW)
    time.sleep(1)
    
    pi.digitalWrite(OUTPUT_PIN,pi.HIGH)
    time.sleep(1)




