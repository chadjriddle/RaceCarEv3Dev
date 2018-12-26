#!/usr/bin/env python3

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from WiiUProLib.WiiUPro import WiiUPro 
from Utils import Log
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

log = Log.Log()
log.msg("starting")

controller = WiiUPro()

controller.Setup(log.msg)
controller.Connect()
controller.Start()

m = LargeMotor(OUTPUT_A)

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return clamp(scale(value,(-1100,1100),(-100,100)), -100, 100)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def motorUpdate(motor, axisValue):
    if axisValue > -12 and axisValue < 12:
        if motor.is_running:
            motor.off(False)
        return # Dead spot
        # log.msg("axisValue: " + str(axisValue))
    else:
        log.msg("axisValue: " + str(axisValue))
        motor.on(axisValue)


while True:
    if controller.Home:
        break
    if controller.A == WiiUPro.PRESSED:
        m.off()

    motorUpdate(m, scale_stick(controller.LeftAxisY))



log.msg("stopping....")
controller.Stop()