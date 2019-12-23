import serial

s=serial.Serial('/dev/tty50',9600,timeout=1)   #ボーレート9600bps
"""
timeoutはシリアルポートをオープンするときのパラメータでreadメソッドのタイムアウト時間を指定することができる
timeout=None    受信完了まで待つ
timeout=0   直ちに処理が返る
timeout=x   x秒後にタイムアウト
"""

for i in range(10):
    gps_data=gps.readline()
    print(gps_data)

"""
ここでコンソール上に現れる文字列はNMEAフォーマットという形式でGPSの生データである
"""
