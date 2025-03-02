from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub

from bluepad import BluePad

bp=BluePad(Port.A)

nr_leds = 3
led_gpio = 12
# change the number of leds and the GPIO pin according to your setup.
bp.neopixel_init(nr_leds, led_gpio)  # initialize neopixels
bp.neopixel_set(0,(20,0,0)) # red pixel
bp.neopixel_set(1,(0,20,0)) # green pixel
bp.neopixel_set(2,(0,0,20)) # blue pixel
