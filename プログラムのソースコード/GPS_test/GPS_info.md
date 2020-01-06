# GPSモジュールとRaspberryPiを接続する際の注意事項
## RaspberryPi側の設定
- serial0からtty1に変更
  1. /boot/cmdline.txtを編集する
    - まずはファイルのバックアップを取っておく(一応)以下をコンソールに打ち込む
      - $ mkdir -p ~/default/boot  <br>
        $ sudo cp -p /boot/cmdline.txt ~/default/boot/ <br>
        $ sudo vi /boot/cmdline.txt  <br>
    - 以下が変更内容
      - #dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=94e60538-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
  2. /boot/config.txtを編集する
    - こちらも一応バックアップ
      - $ sudo cp -p /boot/config.txt ~/default/boot/ <br>
        $ sudo vi /boot/config.txt  <br>
    - 以下を追記
      - enable_uart=1 <br>
        dtoverlay=pps-gpio,gpioin=18  <br>
  3. /etc/moduleを編集する
    - またまたバックアップ
      - $ mkdir ~/default/etc <br>
        $ sudo cp -p /etc/module ~/default/etc/ <br>
        $ sudo vi /etc/module <br>
    - 以下を追記
      - pps-gpio
以上でRaspberryPi側の設定は終わり

## NMEAフォーマット
- GPSから直接送られてくる生データはこのフォーマットで送られてくる
- 文字列になっていてそれぞれ緯度・経度・標高・世界標準時（UTC）などが含まれている 
- 以下$GPRMC

|単語|説明|意味|
|:---|:---|:---|
|085120.307|協定世界時(UTC）での時刻|UTC時刻：08時51分20秒307|<br>
|A|ステータス。V = 警告、A = 有効|ステータス：有効|
|3541.1493|緯度|60分で1度なので、分数を60で割ると度数になります。Googleマップ等で用いられる ddd.dddd度表記は、(度数 + 分数/60) で得ることができます。緯度：35度41.0450分|
|N|北緯か南緯かN = 北緯、South = 南緯|北緯|
|13945.3994|経度|経度；139度45.2337分|
|E|東経か西経かE = 東経、West = 西経|東経|
|000.0|地表における移動の速度000.0～999.9[knot]|移動の速度：000.0[knot]|
|240.3|地表における移動の真方位000.0～359.9度|移動の真方位：240.3度|
|181211|協定世界時(UTC）での日付|UTC日付：2011年12月18日|
|A|モード, N = データなし, A = Autonomous（自律方式）, D = Differential（干渉測位方式）, E = Estimated（推定)|モード：自律方式|
|*6A|チェックサム|チェックサム値：6A|
- その他のフォーマット一覧は[こちら](https://www.hiramine.com/physicalcomputing/arduino/gps_nmeaformat.html)
を参考にする
