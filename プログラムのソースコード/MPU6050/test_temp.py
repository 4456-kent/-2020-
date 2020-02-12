import wiringpi as pi
import time
import mpu6050
import csv

mpu6050_addr=0x68   #Raspberry Pi側のコンソール上で"i2cdetect 1"コマンドで確認
SAMPLING_RATE=10    #サンプリングレート[Hz]
f=open("test_mpu6050_temp.csv","w")
header=['TEMP']

pi.wiringPiSetupGpio()
i2c=pi.I2C()
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
acc.setup()
writer=csv.writer(f,lineterminator="\n")
writer.writerow(header)

for i in range (0,100):
    TEMP=acc.get_temp_value()
    data=[TEMP]
    writer.writerow(data)
    print('{:.3g}'.TEMP)
    time.sleep(1/SAMPLING_RATE)
    
