import wiringpi as pi
servo_pin = 18
set_degree = 90

CYCLE = 20
MIN_PULSE = 0.5
MAX_PULSE = 2.4
MIN_DEG = 0
MAX_DEG = 180
RANGE = 2000

clock = int( 19.2 / float(RANGE) * CYCLE * 1000 )
min_val = RANGE * MIN_PULSE / CYCLE
max_val = RANGE * MAX_PULSE / CYCLE

pi.wiringPiSetupGpio()
pi.pinMode( servo_pin, pi.GPIO.PWM_OUTPUT )
pi.pwmSetMode( pi.GPIO.PWM_MODE_MS )
pi.pwmSetRange( RANGE )
pi.pwmSetClock( clock )

if ( set_degree <= MAX_DEG and set_degree >= MIN_DEG ):
    move_deg = int( ( max_val - min_val ) / MAX_DEG * set_degree )
    pi.pwmWrite( servo_pin, move_deg )
    
