from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = TechnicHub()

from bluepad import BluePad

# Set up a bluepad instance with LMS-ESP32 running Bluepad on port D
bp=BluePad(Port.D)

steer = Motor(Port.A)
fwd = Motor(Port.B)

# Helper to translate values
def scale_stick(val, min_val, max_val, deadzone=25):
    if -deadzone <= val <= deadzone:
        val = 0
    return (float(val + 128) / 256) * (max_val - min_val) + min_val

# Reset steer angle by finding the limit
steer.run_until_stalled(-200, Stop.COAST, 40)
steer.reset_angle(-200)
steer.run_target(300, 0)

while True:
    lx, ly, rx, ry, btns, dpad = bp.gamepad()
    print(lx, ly, rx, ry, btns, dpad)
    if -512 <= lx <= 512: # Gamepad is connected if it returns regular values
        turn = scale_stick(rx, 100,-100)
        spd = scale_stick(ly, 110,-110)
        steer.track_target(turn)
        fwd.dc(spd)
