import wiringpi as pi
import time
import statistics
import mpu6050

mpu6050_addr=0x68

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()

sequence='STAY'

while True:
    if(sequence=='STAY'):
        data=[]
        acc_cnt=0
        while(acc_cnt<5):
            for i in range(0,5):
                data.append(acc.synthetic_acc_cal())
            if(statistics.median(data)>2):
                acc_cnt=acc_cnt+1
            else:
                pass
        if(acc_cnt==5):
            print("OK")
            sequence='LANDING'

    if(sequence=='LANDING'):
        data=[]
        acc_cnt=0
        while(acc_cnt<5):
            for i in range(0,5):
                data.append(acc.synthetic_acc_cal())
            if(statistics.median(data)>2):
                acc_cnt=acc_cnt+1
            else:
                pass
        if(acc_cnt==5):
            print("Finish")
            break
    
    time.sleep(1/100)
