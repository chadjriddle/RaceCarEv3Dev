#!/usr/bin/env python3

from Log import Log
from WiiUPro import WiiUPro 
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor

log = Log()
log.msg("starting")

controller = WiiUPro()

controller.Setup(log.msg)
controller.Connect()
controller.Start()

motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
steering = MediumMotor(OUTPUT_C)

def scale(val, src, dst):
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


    motorUpdate(motorA, -scale_stick(controller.LeftAxisY))
    motorUpdate(motorB, -scale_stick(controller.LeftAxisY))
    motorUpdate(steering, scale_stick(controller.RightAxisX))


log.msg("stopping....")
controller.Stop()