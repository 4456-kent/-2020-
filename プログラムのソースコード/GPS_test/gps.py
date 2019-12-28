import serial
import math

class gps:
    def __init__(self,BAUD_RATE,TIMEOUT,DISTANCE_LAT,DISTANCE_LNG):
       self.BAUD_RATE=BAUD_RATE     #ボーレート[bps]
       self.TIMEOUT=TIMEOUT         #タイムアウト[s]
       self.DISTANCE_LAT=DISTANCE_LAT   #目的地の緯度(ddd.dddd度表記)
       self.DISTANCE_LNG=DISTANCE_LNG   #目的地の経度(ddd.dddd度表記)
    
    def gpgga(self):    #NMEAフォーマットの$GPGGAを取得
        gps_data=[]
        gps_data_str=[]
        
        s=serial.Serial('/dev/ttyS0',self.BAUD_RATE,timeout=self.TIMEOUT)

        for i in range(10):
            gps_data.append(s.readline())
        for i in range(10):
            gps_data_str.append(str(gps_data[i]))
        for i in range(10):
            if(gps_data_str[i][:8]=="b'$GPGGA"):
                (NAME_1,UTC,lat,N_S,lng,W_E,mode,satellite,h_accuracy,alt,m,geoid,m,none,id,checksum)=gps_data_str[i].split(',')
            else:
                pass
        
        return(NAME_1,UTC,lat,N_S,lng,W_E,mode,satellite,h_accuracy,alt,m,geoid,m,none,id,checksum)

    def gprmc(self):    #NMEAフォーマットの$GPRMCを取得
        gps_data=[]
        gps_data_str=[]
        
        s=serial.Serial('/dev/ttyS0',self.BAUD_RATE,timeout=self.TIMEOUT)

        for i in range(10):
            gps_data.append(s.readline())
        for i in range(10):
            gps_data_str.append(str(gps_data[i]))
        for i in range(10):
            if(gps_data_str[i][:8]=="b'$GPRMC"):
                (NAME_2,UTC,STATUS,lat,N_S,lng,W_E,velocity,direction,date,none1,none2,checksum)=gps_data_str[i].split(',')
            else:
                pass
        
        return(NAME_2,UTC,STATUS,lat,N_S,lng,W_E,velocity,direction,date,none1,none2,checksum)

    def gpvtg(self):    #NMEAフォーマットの$GPVTGを取得
        gps_data=[]
        gps_data_str=[]
        
        s=serial.Serial('/dev/ttyS0',self.BAUD_RATE,timeout=self.TIMEOUT)

        for i in range(10):
            gps_data.append(s.readline())
        for i in range(10):
            gps_data_str.append(str(gps_data[i]))
        for i in range(10):
            if(gps_data_str[i][:8]=="b'$GPVTG"):
                (NAME_3,direction,none1,none2,none3,velocity1,n,velocity2,k,checksum)=gps_data_str[i].split(',')
            else:
                pass
        
        return(NAME_3,direction,none1,none2,none3,velocity1,n,velocity2,k,checksum)

    def distance_cal(self): #現在地と目的地までの距離を算出　ヒュベニの公式を利用している
        data=[]

        data=self.gprmc()

        lat_data=float(data[3])/100.0
        lng_data=float(data[5])/100.0

        d_lat_data=int(lat_data)+(lat_data-int(lat_data))*100.0/60.0
        d_lng_data=int(lng_data)+(lng_data-int(lng_data))*100.0/60.0 #緯度・経度を度数表記に変換

        r_DISTANCE_LAT=self.DISTANCE_LAT*math.pi/180.0
        r_DISTANCE_LNG=self.DISTANCE_LNG*math.pi/180.0
        r_lat_data=d_lat_data*(math.pi)/180.0
        r_lng_data=d_lng_data*(math.pi)/180.0 #目的地の緯度経度＆現在の緯度経度をラジアンに変換

        dP=abs(r_DISTANCE_LAT-r_lat_data)   #2点間の緯度差
        dR=abs(r_DISTANCE_LNG-r_lng_data)   #2点間の経度差
        P=dP/2  #2点間の平均緯度

        M=6334834/math.sqrt(pow(3,(1-0.006674*math.sin(P)*math.sin(P)))) #子午線曲率半径
        N=6377397/math.sqrt(1-0.006674*math.sin(P)*math.sin(P)) #卯酉線曲率半径

        D=math.sqrt((M*dP)*(M*dP)+(N*math.cos(P)*dR)*(N*math.cos(P)*dR))    #2点間の距離[m]

        return(D)
    '''
    def direction_cal(self):    #現在地から見た目的地の方角(真北を基準に)
        data=[]

        data=self.gprmc()

        lat_data=float(data[3])/100.0
        lng_data=float(data[5])/100.0

        d_lat_data=int(lat_data)+(lat_data-int(lat_data))*100.0/60.0
        d_lng_data=int(lng_data)+(lng_data-int(lng_data))*100.0/60.0 #緯度・経度を度数表記に変換

        y=(self.DISTANCE_LAT-d_lat_data)*111319.49
        x=(self.DISTANCE_LNG-d_lng_data)*110946.2576

        w=math.atan(x/y)
        
        if(0<=w<=math.pi/2):
            if(0<=float(data[8])<=180.0+w*180.0/math.pi):
                dW=abs(w-float(data[8]))
            elif(180.0+w*180.0/math.pi<float(data[8])<=360):
                dW=abs((360+w*180.0/math.pi)-float(data[8]))
        elif(math.pi/2<w)

        return(dW)
    '''

        


