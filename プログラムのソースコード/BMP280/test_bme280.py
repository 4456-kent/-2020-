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
    alt=weather.altitude_cal()
    print(alt)
    print("[m]\n")
    time.sleep(1)
