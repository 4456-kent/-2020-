import wiringpi as pi

class mpu6050:
 
    def __init__(self,i2c,addr):
        self.addr=addr
        self.i2c=i2c

        self.mpu6050=self.i2c.setup(self.addr)

    def setup(self):
        self.i2c.writeReg8(self.mpu6050,0x1c,0x08)
        self.i2c.writeReg8(self.mpu6050,0x1b,0x08)
        self.i2c.writeReg8(self.mpu6050,0x1a,0x05)

    def get_acc_value(self):
        buf=[]
        ACCEL_SCALE_MODIFIER=8192.0 #加速度のフルスケールを±4Gに設定したときの値
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
        
    def get_gyro_value(self):
        buf=[]
        GYRO_SCALE_MODIFIER=65.5    #角速度のフルスケールを±500deg/sに設定したときの値
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x43+i))
             i=i+1
        
        gyro_x_mesure=((buf[0] << 8) | buf[1])
        gyro_y_mesure=((buf[2] << 8) | buf[3])
        gyro_z_mesure=((buf[4] << 8) | buf[5])

        gyro_x=gyro_x_mesure/GYRO_SCALE_MODIFIER
        gyro_y=gyro_y_mesure/GYRO_SCALE_MODIFIER
        gyro_z=gyro_z_mesure/GYRO_SCALE_MODIFIER

        return(gyro_x,gyro_y,gyro_z)

   