"""

本ファイルはMPU6050のpythonのlib
データシート：https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf
アドレスマップ：https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf

"""

import wiringpi as pi

class mpu6050:
 
    def __init__(self,i2c,addr):       #I2Cの初期化
        self.addr=addr
        self.i2c=i2c

        self.mpu6050=self.i2c.setup(self.addr)

    def setup(self):    #最初のI2Cの書き込み
        self.i2c.writeReg8(self.mpu6050,0x6b,0x01)  #Bit6のSLEEPをLOWにしないと値が0しか返ってこなくなる
        self.i2c.writeReg8(self.mpu6050,0x1c,0x08)  #Full Scale Rangeを±4Gに設定
        self.i2c.writeReg8(self.mpu6050,0x1b,0x08)  #Full Scale Rangeを±500deg/sに設定
        self.i2c.writeReg8(self.mpu6050,0x1a,0x02)  #フィルターを約96Hzに設定


    def get_acc_value(self):    #加速度の値取得
        buf=[]
        ACCEL_SCALE_MODIFIER=8192.0 #Full Scale Rangeを±4Gに設定したときの値
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x3b+i))
             i=i+1
        
        acc_x_mesure=((buf[0] << 8) | buf[1])
        acc_y_mesure=((buf[2] << 8) | buf[3])
        acc_z_mesure=((buf[4] << 8) | buf[5])

        acc_x=acc_x_mesure/ACCEL_SCALE_MODIFIER
        acc_y=acc_y_mesure/ACCEL_SCALE_MODIFIER
        acc_z=acc_z_mesure/ACCEL_SCALE_MODIFIER
        
        return(acc_x,acc_y,acc_z)

    def get_temp_value(self):   #気温の値を取得
        buf=[]
        i=0
        while(i<2):
            buf.append(self.i2c.readReg8(self.mpu6050,0x41+1))
            i=i+1

        temp_mesure=((buf[0] << 8) | buf[1])

        temp=temmp_mesure/340+36.53

        return(temp)
        
    def get_gyro_value(self):   #角速度の値を取得
        buf=[]
        GYRO_SCALE_MODIFIRE=65.5    ##Full Scale Rangeを±500deg/sに設定したときの値
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x43+i))
             i=i+1
        
        gyro_x_mesure=((buf[0] << 8) | buf[1])
        gyro_y_mesure=((buf[2] << 8) | buf[3])
        gyro_z_mesure=((buf[4] << 8) | buf[5])

        gyro_x=gyro_x_mesure/GYRO_SCALE_MODIFIRE
        gyro_y=gyro_y_mesure/GYRO_SCALE_MODIFIRE
        gyro_z=gyro_z_mesure/GYRO_SCALE_MODIFIRE

        return(gyro_x,gyro_y,gyro_z)

   