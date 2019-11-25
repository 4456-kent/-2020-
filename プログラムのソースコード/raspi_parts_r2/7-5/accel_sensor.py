import wiringpi as pi
import time
import lis3dh

SPI_CS = 0

SPI_SPEED = 100000

pi.wiringPiSPISetup (SPI_CS, SPI_SPEED)

accel = lis3dh.lis3dh( SPI_CS )

while True:
    ( x, y, z ) = accel.get_accel()
    print ("x:", x, "  y:", y, "  z:", z)

    time.sleep(1)
