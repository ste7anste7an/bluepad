from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub

from bluepad import BluePad

bp=BluePad(Port.A)

servo_nr=2 # attach servo signal to GPIO21 on LMS_ESP32v2

for x in range(5000):
     bp.servo(servo_nr, x%180)
     print(bp.gamepad())
