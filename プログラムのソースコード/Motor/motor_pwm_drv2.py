import time
import wiringpi as pi

motor1_1_pin=23
motor1_2_pin=24

motor2_1_pin=5
motor2_2_pin=6

pi.wiringPiSetupGpio()
pi.pinMode(motor1_1_pin,pi.OUTPUT)
pi.pinMode(motor1_2_pin,pi.OUTPUT)
pi.pinMode(motor2_1_pin,pi.OUTPUT)
pi.pinMode(motor2_2_pin,pi.OUTPUT)

pi.softPwmCreate(motor1_1_pin,0,100)
pi.softPwmCreate(motor1_2_pin,0,100)
pi.softPwmCreate(motor2_1_pin,0,100)
pi.softPwmCreate(motor2_2_pin,0,100)

pi.softPwmWrite(motor1_1_pin,0)
pi.softPwmWrite(motor1_2_pin,0)
pi.softPwmWrite(motor2_1_pin,0)
pi.softPwmWrite(motor2_2_pin,0)

while True:
    speed=0
    while(speed<=100):
        pi.softPwmWrite(motor1_1_pin,speed)
        pi.softPwmWrite(motor1_2_pin,0)
        pi.softPwmWrite(motor2_1_pin,speed)
        pi.softPwmWrite(motor2_2_pin,0)
        time.sleep(0.5)
        speed=speed+1

    pi.softPwmWrite(motor1_1_pin,100)
    pi.softPwmWrite(motor1_2_pin,100)   #モーターの両端子に100%の出力を書けることでブレーキとする
    pi.softPwmWrite(motor2_1_pin,100)
    pi.softPwmWrite(motor2_2_pin,100)
    time.sleep(2)

    speed=0
    while(speed<=100):
        pi.softPwmWrite(motor1_1_pin,0)
        pi.softPwmWrite(motor1_2_pin,speed)
        pi.softPwmWrite(motor2_1_pin,0)
        pi.softPwmWrite(motor2_2_pin,speed)
        time.sleep(0.5)
        speed=speed+1

    pi.softPwmWrite(motor1_1_pin,0)
    pi.softPwmWrite(motor1_2_pin,0)
    pi.softPwmWrite(motor2_1_pin,0)
    pi.softPwmWrite(motor2_2_pin,0)
    time.sleep(2)
