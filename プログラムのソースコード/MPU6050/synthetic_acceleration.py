import mpu6050
import wiringpi as pi
import time

mpu6050_addr=0x68
SAMPLING_RATE=50

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()

while True:
    data=acc.synthetic_acc_cal()
    print(data)
    print("[G]\n")
    time.sleep(1/SAMPLING_RATE)

