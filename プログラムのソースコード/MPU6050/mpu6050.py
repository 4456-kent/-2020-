"""

本ファイルはMPU6050のpythonのlib
データシート：https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf
アドレスマップ：https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf

"""

import wiringpi as pi
import time

class mpu6050:
 
    def __init__(self,i2c,addr):       #I2Cの初期化
        self.addr=addr
        self.i2c=i2c

        self.mpu6050=self.i2c.setup(self.addr)

    def setup(self):    #最初のI2Cの書き込み
        self.i2c.writeReg8(self.mpu6050,0x6b,0x80)  #デバイスリセット
        time.sleep(0.25)
        self.i2c.writeReg8(self.mpu6050,0x6b,0x00)  #6bit目を0にしておかないとスリープモードに移行する
        time.sleep(0.25)
        self.i2c.writeReg8(self.mpu6050,0x6a,0x07)  
        time.sleep(0.25)
        self.i2c.writeReg8(self.mpu6050,0x6a,0x00)
        time.sleep(0.25)
        self.i2c.writeReg8(self.mpu6050,0x1c,0x08)  #Full Scale Rangeを±4Gに設定
        self.i2c.writeReg8(self.mpu6050,0x1b,0x08)  #Full Scale Rangeを±500deg/sに設定
        self.i2c.writeReg8(self.mpu6050,0x1a,0x00)  #config


    def get_acc_value(self):    #加速度の値取得
        buf=[]
        ACCEL_SCALE_MODIFIER=8192.0 #Full Scale Rangeを±4Gに設定したときの値
        ACCEL_RANGE=4.0
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x3b+i))
             i=i+1
        
        acc_x_mesure=((buf[0] << 8) | buf[1])
        acc_y_mesure=((buf[2] << 8) | buf[3])
        acc_z_mesure=((buf[4] << 8) | buf[5])

        if(acc_x_mesure<=ACCEL_SCALE_MODIFIER*ACCEL_RANGE):
            acc_x=acc_x_mesure/ACCEL_SCALE_MODIFIER
        elif(acc_x_mesure>ACCEL_SCALE_MODIFIER*ACCEL_RANGE):
            acc_x=acc_x_mesure/ACCEL_SCALE_MODIFIER-ACCEL_RANGE*2
            
        if(acc_y_mesure<=ACCEL_SCALE_MODIFIER*ACCEL_RANGE):
            acc_y=acc_y_mesure/ACCEL_SCALE_MODIFIER
        elif(acc_y_mesure>ACCEL_SCALE_MODIFIER*ACCEL_RANGE):
            acc_y=acc_y_mesure/ACCEL_SCALE_MODIFIER-ACCEL_RANGE*2

        if(acc_z_mesure<=ACCEL_SCALE_MODIFIER*ACCEL_RANGE):
            acc_z=acc_z_mesure/ACCEL_SCALE_MODIFIER
        elif(acc_z_mesure>ACCEL_SCALE_MODIFIER*ACCEL_RANGE):
            acc_z=acc_z_mesure/ACCEL_SCALE_MODIFIER-ACCEL_RANGE*2
            
        return(acc_x,acc_y,acc_z)

    def get_temp_value(self):   #気温の値を取得
        buf=[]
        i=0
        while(i<2):
            buf.append(self.i2c.readReg8(self.mpu6050,0x41+i))
            i=i+1

        temp_mesure=((buf[0] << 8) | buf[1])

        temp=(temp_mesure-53584.74)/370.85

        return(temp)
        
    def get_gyro_value(self):   #角速度の値を取得
        buf=[]
        GYRO_SCALE_MODIFIRE=65.5    #Full Scale Rangeを±500deg/sに設定したときの値
        GYRO_RANGE=500
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x43+i))
             i=i+1
        
        gyro_x_mesure=((buf[0] << 8) | buf[1])
        gyro_y_mesure=((buf[2] << 8) | buf[3])
        gyro_z_mesure=((buf[4] << 8) | buf[5])

        if(gyro_x_mesure<=GYRO_SCALE_MODIFIRE*GYRO_RANGE):      #加速度・角速度ともに0未満になるときはフルレンジの2倍した値を引かなければならない
            gyro_x=gyro_x_mesure/GYRO_SCALE_MODIFIRE
        elif(gyro_x_mesure>GYRO_SCALE_MODIFIRE*GYRO_RANGE):
            gyro_x=gyro_x_mesure/GYRO_SCALE_MODIFIRE-GYRO_RANGE*2

        if(gyro_y_mesure<=GYRO_SCALE_MODIFIRE*GYRO_RANGE):
            gyro_y=gyro_y_mesure/GYRO_SCALE_MODIFIRE
        elif(gyro_y_mesure>GYRO_SCALE_MODIFIRE*GYRO_RANGE):
            gyro_y=gyro_y_mesure/GYRO_SCALE_MODIFIRE-GYRO_RANGE*2

        if(gyro_z_mesure<=GYRO_SCALE_MODIFIRE*GYRO_RANGE):
            gyro_z=gyro_z_mesure/GYRO_SCALE_MODIFIRE
        elif(gyro_z_mesure>GYRO_SCALE_MODIFIRE*GYRO_RANGE):
            gyro_z=gyro_z_mesure/GYRO_SCALE_MODIFIRE-GYRO_RANGE*2

        return(gyro_x,gyro_y,gyro_z)

   