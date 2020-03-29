import wiringpi as pi
import time
import csv
import mpu6050
import statistics

mpu6050_addr=0x68

DROP_ACC=0.2  #落下判定の閾値[G]
LANDING_ACC=2.5 #着地判定の閾値[G]

acc_cnt1=0
acc_cnt2=0
SEQUENCE='STAY'

def log():
    t=time.time()-t0
    data=acc.synthetic_acc_cal()

    line=[t,data,SEQUENCE]

    writer.writerow(line)

f=open("measure_acceleration_ver2.csv","w")
header=["TIME","ACCELERATION","SEQUENCE"]

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()
writer=csv.writer(f,lineterminator="\n")
writer.writerow(header)

time.sleep(30)

t0=time.time()

while (SEQUENCE=='STAY'):       #落下判定シーケンス
    drop_synthetic_acc=[]
    log()
    if(acc_cnt1<5):
        for i in range(0,3):
            drop_synthetic_acc.append(acc.synthetic_acc_cal())
        if(statistics.median(drop_synthetic_acc)<=DROP_ACC):
            acc_cnt1=acc_cnt1+1
        else:
            pass
    elif(acc_cnt1==5):
        t1=time.time()-t0
        SEQUENCE='DROP'
        break

while (SEQUENCE=='DROP'):       #着地判定シーケンス
    landing_synthetic_acc=[]
    log()
    if(acc_cnt2<5):
        for i in range(0,3):
            landing_synthetic_acc.append(acc.synthetic_acc_cal())
        if(statistics.median(landing_synthetic_acc)>LANDING_ACC):
            acc_cnt2=acc_cnt2+1
        else:
            pass
    elif(acc_cnt2==5):
        t2=time.time()-t0
        SEQUENCE='LANDING'
        break

if(SEQUENCE=='LANDING'):
     writer.writerow(['END'])
     f.close()