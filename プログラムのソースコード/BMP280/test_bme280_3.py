import bme280
import wiringpi as pi
import statistics
import time

bme280_addr=0x76

pi.wiringPiSetupGpio()
i2c=pi.I2C()
weather=bme280.bme280(i2c,bme280_addr,1013)
weather.setup()

s_press_sample=[]
for i in range(0,100):
    s_press_sample.append(weather.get_press_value())

s_press=statistics.median(s_press_sample)

weather=bme280.bme280(i2c,bme280_addr,s_press)
weather.setup()

while True:
    alt_bf=[]
    alt_af=[]
    for i in range(0,3):
        alt_bf.append(weather.altitude_cal())
    time.sleep(0.02)
    for i in range(0,3):
        alt_af.append(weather.altitude_cal())
    diff=statistics.median(alt_af)-statistics.median(alt_bf)

    if(diff<-1):
        print("DROP\n")

