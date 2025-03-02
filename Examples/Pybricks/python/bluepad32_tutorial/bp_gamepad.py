from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub

from bluepad import BluePad

bp=BluePad(Port.A)

while True:
   print(bp.gamepad())
