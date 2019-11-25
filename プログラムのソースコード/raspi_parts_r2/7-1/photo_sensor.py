import wiringpi as pi
import time
import mcp_adc

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

adc = mcp_adc.mcp3002( SPI_CE, SPI_SPEED, VREF )

while True:
    value = adc.get_value( READ_CH )
    print ("Value:", value )

    time.sleep( 0.1 )


