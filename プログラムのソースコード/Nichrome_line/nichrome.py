
import time
import wiringpi as pi

NICHROME_PIN=23
SWITCH_PIN=24
TIME=5

pi.wiringPiSetupGpio()
pi.pinMode(NICHROME_PIN,pi.OUTPUT)
pi.pinMode(SWITCH_PIN,pi.INPUT)

pi.digitalWrite(NICHROME_PIN,pi.LOW)

while True:
    if(pi.digitalRead(SWITCH_PIN)==0):
        pi.digitalWrite(NICHROME_PIN,pi.HIGH)
        time.sleep(TIME)
        pi.digitalWrite(NICHROME_PIN,pi.LOW)
        break
    elif(pi.digitalRead(SWITCH_PIN)==1):
        pass


