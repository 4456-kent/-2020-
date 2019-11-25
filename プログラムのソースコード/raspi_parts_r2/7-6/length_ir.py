import wiringpi as pi
import time
import gp2y0e03

GP2Y0E03_ADDR = 0x40

i2c = pi.I2C()

ir_dev = gp2y0e03.gp2y0e03( i2c, GP2Y0E03_ADDR )

time.sleep(1)

while True:
    distance = ir_dev.read_distance()

    print ("Distance:", distance , "cm" )

    time.sleep(1)
