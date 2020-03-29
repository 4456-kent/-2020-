import wiringpi as pi
import time
import statistics
import mpu6050

mpu6050_addr=0x68

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()

to=time.time()
array=[]
for i in range(0,3):
    array.append(acc.synthetic_acc_cal())
if(statistics.median(array)>2):
    pass
else:
    pass
t1=time.time()-to
print(statistics.median(array))
print("\n")
print(t1)



