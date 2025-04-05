from hub import light_matrix
from hub import port
from hub import light_matrix

import color_sensor
import runloop
import time

def gamepad():
    """ read the color values of the simulated color sensor to obtain the reading of the gamepad"""
    i,r,g,b=color_sensor.rgbi(port.A)
    button=i%256
    dpad=i//156
    lx=r%256
    ly=r//256
    rx=g%256
    ry=g//256
    return (lx,ly,rx,ry,button,dpad)
    

async def main():
    # write your code here
    while True:
        lx,ly,rx,ry,button,dpad=gamepad()
        light_matrix.clear()
        light_matrix.set_pixel(lx//62, ly//62, 100)        
        light_matrix.set_pixel(rx//62, ry//62, 60)
        time.sleep_ms(50)
        #light_matrix.show()
runloop.run(main())
