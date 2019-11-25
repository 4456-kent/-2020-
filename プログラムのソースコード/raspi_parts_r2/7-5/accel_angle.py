import wiringpi as pi
import time, math
import lis3dh

SPI_CS = 0

SPI_SPEED = 100000

pi.wiringPiSPISetup (SPI_CS, SPI_SPEED)

accel = lis3dh.lis3dh( SPI_CS )

while True:
    ( x, y, z ) = accel.get_accel()

    x_angle = math.degrees( math.atan2( x, math.sqrt( y ** 2 + z ** 2 ) ) )
    y_angle = math.degrees( math.atan2( y, math.sqrt( x ** 2 + z ** 2 ) ) )

    print ("X Angle:", x_angle, "  Y Angle:", y_angle )

    time.sleep(1)
