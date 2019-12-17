import serial
import math

class gps:
    gps_data=[]

    def __init__(self,BAUD_RATE,TIMEOUT):
        self.BAUD_RATE=BAUD_RATE
        self.TIMEOUT=TIMEOUT
        
        self.gps=GPS.Serial('/dev/tty50',self.BAUD_RATE,timeout=self.TIMEOUT)

    def setup(self,DISTANCE_LAT,DISTANCE_LNG):
        self.DISTANCE_LAT=DISTANCE_LAT
        self.DISTANCE_LNG=DISTANCE_LNG


    def gps_read(self):
        for i in range(10):
            gps_data[i]=GPS.readline()

    def gpgga(self):
        (UTC,lat,N_S,lng,W_E,mode,satellite,h_accuracy,alt,m,geoid,m,none,id,checksum)=gps_data[0].split(',')
        return(UTC,lat,N_S,lng,W_E,mode,satellite,h_accuracy,alt,m,geoid,m,none,id,checksum)

    def gprmc(self):
        (UTC,lat,N_S,lng,W_E,velocity,direction,date,none1,none2,mode,checksum)=gps_data[7].split(',')
        return(UTC,lat,N_S,lng,W_E,velocity,direction,date,none1,none2,mode,checksum)

    def gpvtg(self):
        (direction,none1,none2,none3,velocity1,n,velocity2,k,mode,checksum)=gps_data[8].split(',')
        return(direction,none1,none2,none3,velocity1,n,velocity2,k,mode,checksum)

    def distance_cal(self): #ヒュベニの公式を利用している
        data=gprmc()

        lat_data=data[1]
        lng_data=data[3]

        d1=lat_data.split('.')
        d2=lng_data.split('.')

        d_lat_data=d1[0]+(d1[1]/60)
        d_lng_data=d2[0]+(d2[1]/60) #緯度・経度を度数表記に変換

        r_DISTANCE_LAT=self.DISTANCE_LAT*math.pi/180
        r_DISTANCE_LNG=self.DISTANCE_LNG*math.pi/180
        r_lat_data=d_lat_data*(math.pi)/180
        r_lng_data=d_lng_data*(math.pi)/180 #目的地の緯度経度＆現在の緯度経度をラジアンに変換

        dP=abs(r_DISTANCE_LAT-r_lat_data)   #2点間の緯度差
        dR=abs(r_DISTANCE_LNG-r_lng_data)   #2点間の経度差
        P=dP/2  #2点間の平均緯度

        M=6334834/math.sqrt((1-0.006674*math.sin(P)*math.sin(P))^3) #子午線曲率半径
        N=6377397/math.sqrt(1-0.006674*math.sin(P)*math.sin(P)) #卯酉線曲率半径

        D=math.sqrt((M*dP)*(M*dP)+(N*math.cos(P)*dR)*(N*math.cos(P)*dR))    #2点間の距離[m]

        return(D)



        


