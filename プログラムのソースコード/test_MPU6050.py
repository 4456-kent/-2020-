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
    (acc_x,acc_y,acc_z)=acc.get_accel_data()
    (gyro_x,gyro_y,gyro_z)=acc.get_gyro_data()
    print("ACC_X:",acc_x,"ACC_Y:",acc_y,"ACC_Z:",acc_z,"\n")
    print("GYRO_X:",gyro_x,"GYRO_Y:",gyro_y,"GYRO_Z",gyro_z,"\n")
    time.sleap(1)




