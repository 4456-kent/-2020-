"""  以下MPU6050のメモリーマップ      
        SELF_TEST_X			= 0x0D, // RW

		SELF_TEST_Y,

		SELF_TEST_Z,

		SELF_TEST_A,

		SMPLRT_DIV			= 0x19, // RW

		CONFIG				= 0x1A, // RW

		GYRO_CONFIG,

		ACCEL_CONFIG,

		FIFO_EN				= 0x23, // RW

		I2C_MST_CTRL		= 0x24, // RW

		I2C_SLV0_ADDR		= 0x25, // RW

		I2C_SLV0_REG,

		I2C_SLV0_CTRL,

		I2C_SLV1_ADDR		= 0x28, // RW

		I2C_SLV1_REG,

		I2C_SLV1_CTRL,

		I2C_SLV2_ADDR		= 0x2B, // RW

		I2C_SLV2_REG,

		I2C_SLV2_CTRL,

		I2C_SLV3_ADDR		= 0x2E, // RW

		I2C_SLV3_REG,

		I2C_SLV3_CTRL,

		I2C_SLV4_ADDR		= 0x31, // RW

		I2C_SLV4_REG,

		I2C_SLV4_DO,

		I2C_SLV4_CTRL,

		I2C_SLV4_DI			= 0x35, // R

		I2C_MST_STATUS		= 0x36, // R

		INT_PIN_CFG			= 0x37, // RW

		INT_ENABLE,

		INT_STATUS			= 0x3A, // R

		ACCEL_XOUT_H		= 0x3B, // R

		ACCEL_XOUT_L,

		ACCEL_YOUT_H,

		ACCEL_YOUT_L,

		ACCEL_ZOUT_H,

		ACCEL_ZOUT_L,

		TEMP_OUT_H,

		TEMP_OUT_L,

		GYRO_XOUT_H,

		GYRO_XOUT_L,

		GYRO_YOUT_H,

		GYRO_YOUT_L,

		GYRO_ZOUT_H,

		GYRO_ZOUT_L,

//		EXT_SENS_DATA_00	= 0x49, // R

//		EXT_SENS_DATA_01,

//		...

//		EXT_SENS_DATA_23,

		EXT_SENS_DATA_START	= 0x49, // R (0~23)

		EXT_SENS_DATA_END	= EXT_SENS_DATA_START + 23,

		I2C_SLV0_DO			= 0x63, // RW

		I2C_SLV1_DO,

		I2C_SLV2_DO,

		I2C_SLV3_DO,

		I2C_MST_DELAY_CTRL	= 0x67, // RW

		SIGNAL_PATH_RESET	= 0x68, // RW

		USER_CTRL			= 0x6A, // RW

		PWR_MGMT_1			= 0x6B, // RW

		PWR_MGMT_2,

		FIFO_COUNT_H		= 0x72, // RW

		FIFO_COUNT_L,

		FIFO_R_W			= 0x74, // RW

		WHO_AM_I			= 0x75, // R    
"""

import wiringpi as pi

class mpu6050:
    ACCEL_SCALE_MODIFIER=8192.0 #加速度のフルスケールを±4Gに設定したときの値
    GYRO_SCALE_MODIFIER=65.5    #各速度のフルスケールを±500deg/sに設定したときの値

    def __init__(self,i2c,addr):
        self.addr=addr
        self.i2c=i2c
        self.t_fine=0.0

        self.mpu6050=self.i2c.setup(self.addr)

    def setup(self):
        self.i2c.writeReg8(self.mpu6050,0x1b,0x08)
        self.i2c.writeReg8(self.mpu6050,0x1c,0x08)
        self.i2c.writeReg8(self.mpu6050,0x1a,0x02)

    def get_value(self):
        buf=[]
        for i in range(0x3b,0x3c):
            buf.append(self.i2c.readReg8(self.mpu6050,i))
        for i in range(0x3d,0x3e):
            buf.append(self.i2c.readReg8(self.mpu6050,i))
        for i in range(0x3f,0x40):
            buf.append(self.i2c.readReg8(self.mpu6050,i))
        for  i in range(0x43,0x44):
            buf.append(self.i2c.readReg8(self.mpu6050,i))
        for  i in range(0x45,0x46):
            buf.append(self.i2c.readReg8(self.mpu6050,i))
        for  i in range(0x47,0x48):
            buf.append(self.i2c.readReg8(self.mpu6050,i))

        acc_x_mesure=((buf[0] << 8) | buf[1])
        acc_y_mesure=((buf[2] << 8) | buf[3])
        acc_z_mesure=((buf[4] << 8) | buf[5])
        gyro_x_mesure=((buf[6] <<8) | buf[7])
        gyro_y_mesure=((buf[8] << 8) | buf[9])
        gyro_z_mesure=((buf[10] << 8) | buf[11])

        acc_x=acc_x_mesure/ACCEL_SCALE_MODIFIER
        acc_y=acc_y_mesure/ACCEL_SCALE_MODIFIER
        acc_z=acc_z_mesure/ACCEL_SCALE_MODIFIER
        gyro_x=gyro_x_mesure/GYRO_SCALE_MODIFIER
        gyro_y=gyro_y_mesure/GYRO_SCALE_MODIFIER
        gyro_z=gyro_z_mesure/GYRO_SCALE_MODIFIER

        return(acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z)
