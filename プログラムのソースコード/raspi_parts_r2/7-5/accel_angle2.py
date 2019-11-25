import wiringpi as pi
import time
import lis3dh

SPI_CS = 0

SPI_SPEED = 100000

pi.wiringPiSPISetup (SPI_CS, SPI_SPEED)

accel = lis3dh.lis3dh( SPI_CS )

while True:
    ( x_angle, y_angle ) = accel.get_angle()
    print ("X Angle:", x_angle, "  Y Angle:", y_angle )

    time.sleep(1)
