import wiringpi as pi
import time
import mpu6050

mpu6050_addr=0x68   #Raspberry Pi側のコンソール上で"i2cdetect 1"コマンドで確認
SAMPLING_RATE=10    #サンプリングレート[Hz]

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()

while True:
    (acc_x,acc_y,acc_z)=acc.get_acc_value()
    (temp)=acc.get_temp_value()
    (gyro_x,gyro_y,gyro_z)=acc.get_gyro_value()

    print("ACC_X:",acc_x,"ACC_Y:",acc_y,"ACC_Z:",acc_z,"\n")
    print("TEMP:",temp,"\n")
    print("GYRO_X:",gyro_x,"GYRO_Y:",gyro_y,"GYRO_Z:",gyro_z,"\n")
    print("\n")

    time.sleep(1/SAMPLING_RATE)