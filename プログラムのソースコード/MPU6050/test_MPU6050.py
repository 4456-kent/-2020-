import wiringpi as pi
import time
import mpu6050

mpu6050_addr=0x68

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.set_accel_range()
acc.set_gyro_range()

while True:
    (acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z)=acceleration.get_value()

    print(acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z)
    time.sleep(1/SAMPLING_RATE)