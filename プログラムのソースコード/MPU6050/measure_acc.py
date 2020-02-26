import wiringpi as pi
import time
import csv
import mpu6050

mpu6050_addr=0x68
SAMPLING_RATE=50

f=open("mesure_acceleration.csv","w")
header=["TIME","ACCELERATION"]

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()
writer=csv.writer(f,lineterminator="\n")
writer.writerow(header)

time.sleep(30)

t0=time.time()
while True:
    t=time.time()-t0
    data=acc.synthetic_acc_cal()

    line=[t,data]

    writer.writerow(line)

    time.sleep(1/SAMPLING_RATE)

    if(t>30):
        writer.writerow(['END'])
        f.close()
        break
