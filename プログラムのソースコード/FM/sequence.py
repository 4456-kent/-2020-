
import wiringpi as pi
import time
import datetime
import serial
import picamera
import csv
import statistics
import mpu6050
import bme280
import gps

mpu6050_addr=0x68   #MPU6050のアドレス

bme280_addr = 0x76  #BME280のアドレス

BAUD_RATE=9600  #GPSボーレート9600bps
TIMEOUT=1   #GPSタイムアウト1[s]
DISTANCE_LAT=35.6185408     #目標地点の緯度
DISTANCE_LNG=139.3850305    #目標地点の経度

SAMPLING_RATE=50    #サンプリングレート[Hz]
s=press=1013    #地表面の大気圧[hPa]
DROP_ACCELERATION=1     #落下判定条件[G]
LANDING_ACCELERATION=3  #着地判定条件[G]
LANDING_TIME=10     #着地判定のタイムアウト[s]

MOTOR_R_1PIN=23
MOTOR_R_2PIN=24     #右輪モーター制御のGPIOピン番号
MOTOR_L_1PIN=5
MOTOR_L_2PIN=6      #左輪モーター制御のGPIOピン番号

t0=time.time()      #基準時

today_date=datetime.date.today()    #ログのセットアップ
filename='log'+today_date+'.csv'
f=open(filename,"w")
header=['TIME','ACCELERATION','ALTITUDE','LATITUDE','LONGITUDE','DISTANCE']
writer=csv.writer(f,lineterminator="\n")
writer.writerow(header)

location=gps.gps(BAUD_RATE,TIMEOUT,DISTANCE_LAT,DISTANCE_LNG)   #GPSのセットアップ

pi.wiringPiSetupGpio()  #GPIOピンのセットアップ

i2c=pi.I2C()            #BME280とMPU6050のセットアップ
acc=mpu6050.mpu6050(i2c,mpu6050_addr)
press=bme280.bme280(i2c,bmp280_addr,s_press)
acc.setup()
press.setup()       

pi.pinMode(MOTOR_R_1PIN,pi.OUTPUT)      #駆動部のセットアップ
pi.pinMode(MOTOR_R_2PIN,pi.OUTPUT)
pi.pinMode(MOTOR_L_1PIN,pi.OUTPUT)
pi.pinMode(MOTOR_L_2PIN,pi.OUTPUT)
pi.softPwmCreate(MOTOR_R_1PIN,0,100)
pi.softPwmCreate(MOTOR_R_2PIN,0,100)
pi.softPwmCreate(MOTOR_L_1PIN,0,100)
pi.softPwmCreate(MOTOR_L_2PIN,0,100)
pi.softPwmWrite(MOTOR_R_1PIN,0)
pi.softPwmWrite(MOTOR_R_2PIN,0)
pi.softPwmWrite(MOTOR_L_1PIN,0)
pi.softPwmWrite(MOTOR_L_2PIN,0)  


while True:
    t=time.time()
    dt=t-t0

    synthetic_acc=acc.synthetic_acc_cal()
    altitude=press.alititude_cal()
    
    gprmc_data=[]
    gprmc_data=location.gprmc()
    lat_data=float(data[3])/100.0
    lng_data=float(data[5])/100.0
    latitude=int(lat_data)+(lat_data-int(lat_data))*100.0/60.0
    longitude=int(lng_data)+(lng_data-int(lng_data))*100.0/60.0 

    distance=location.distance_cal

    log=[dt,synthetic_acc,altitude,latitude,longitude,distance]
    writer.writerow(log)

    time.sleep(1/SAMPLING_RATE)

    if (distance<0.5):      #log終了条件は要検討
        f.close()
        break


while True:     #クレーン上昇フェーズ
    altitude=press.altitude_cal()
    time.sleep(1/SAMPLING_RATE)

    if(altitude>25):
        break

while True:     #落下判定
    altitude_b=[]
    altitude_a=[]
    drop_synthetic_acc=[]
    for i in range(0,5):
        altitude_b.append(press.altitude_cal())
        drop_synthetic_acc.append(acc.synthetic_acc_cal())

    for j in range(0,5):
        altitude_a.append(press.altitude_cal())

    acc_cnt=0
    alt_cnt=0
    while(acc_cnt<5):
        if(statistics.median(drop_synthetic_acc)>=DROP_ACCELERATION):
            acc_cnt=acc_cnt+1
        else:
            pass

    while(alt_cnt<5):
        if(statistics.median(altitude_a)-statistics.median(altitude_b)<0):
            alt_cnt=alt_cnt+1
        else:
            pass

    if(acc_cnt==4 or alt_cnt==4 ):
        t1=time.time()
        break

    time.sleep(1/SAMPLING_RATE)

while True:     #着地判定
    landing_synthetic_acc=[]
    for i in range(0,5):
        landing_synthetic_acc.append(acc.synthetic_acc_cal())

    acc_cnt=0
    while(acc_cnt<5):
        if(statistics.median(landing_synthetic_acc)>=LANDING_ACCELERATION):
            acc_cnt=acc_cnt+1
        else:
            pass

    if(acc_cnt==4 or time.time()-t1>=LANDING_TIME):
        #ここで車輪展開
        time.sleep(2)
        break

    time.sleep(1/SAMPLING_RATE)
