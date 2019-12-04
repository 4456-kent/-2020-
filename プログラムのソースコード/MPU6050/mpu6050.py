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
        
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x3b+i))
             i=i+1
        
        acc_x_mesure=((buf[0] << 8) | buf[1])
        acc_y_mesure=((buf[2] << 8) | buf[3])
        acc_z_mesure=((buf[4] << 8) | buf[5])

        acc_x=acc_x_mesure
        acc_y=acc_y_mesure
        acc_z=acc_z_mesure
        
        return(acc_x,acc_y,acc_z)
        
    def get_gyro_value(self):
        buf=[]
        
        i=0
        while(i<6):
             buf.append(self.i2c.readReg8(self.mpu6050,0x43+i))
             i=i+1
        
        gyro_x_mesure=((buf[0] << 8) | buf[1])
        gyro_y_mesure=((buf[2] << 8) | buf[3])
        gyro_z_mesure=((buf[4] << 8) | buf[5])

        gyro_x=gyro_x_mesure
        gyro_y=gyro_y_mesure
        gyro_z=gyro_z_mesure

        return(gyro_x,gyro_y,gyro_z)

   