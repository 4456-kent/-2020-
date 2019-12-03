import wiringpi as pi

class mpu6050:
    def __init__(self,i2c,addr):
        self.addr=addr
        self.i2c=i2c
        self.cd_acc_x=[]
        self.cd_acc_y=[]
        self.cd_acc_z=[]
        self.cd_gyro_x=[]
        self.cd_gyro_y=[]
        self.cd_gyro_z=[]
        self.t_fine=0.0

        self.mpu6050=self.i2c.setup(self.addr)



