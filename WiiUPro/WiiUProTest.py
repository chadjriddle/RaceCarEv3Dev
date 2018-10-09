#!/usr/bin/env python3
__author__ = 'Anton Vanhoucke'

import evdev
import ev3dev.auto as ev3
import threading

logf = open("process.log", "w")

def log(message):
    logf.write(message + "\n")
    logf.flush()
    print(message)

## Some helpers ##
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
    return scale(value,(0,255),(-100,100))

## Initializing ##
log("Finding WiiU Pro controller...")
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    log("Device: " + device.name)
    if device.name == 'Nintendo Wii Remote Pro Controller':
        log("Controller Found!")
        ps3dev = device.fn

gamepad = evdev.InputDevice(ps3dev)

speed = 0
speedMax = 100
speedMin = 0
running = False
backward = False

class MotorThread(threading.Thread):
    def __init__(self):
        self.motor = ev3.LargeMotor(ev3.OUTPUT_A)
        threading.Thread.__init__(self)

    def run(self):
        print("Engine running!")
        while True:
            while running:
                actual_speed = -speed if backward else speed
                self.motor.run_direct(duty_cycle_sp=actual_speed)

            self.motor.stop()

motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()

LeftCenterYMin = -70
LeftCenterYMax = 70
LeftCenterXMin = -70
LeftCenterXMax = 70

RightCenterYMin = -70
RightCenterYMax = 70
RightCenterXMin = -70
RightCenterXMax = 70

LeftYMax = 0
LeftYMin = 0
LeftXMax = 0
LeftXMin = 0

RightYMax = 0
RightYMin = 0
RightXMax = 0
RightXMin = 0

for event in gamepad.read_loop():   #this loops infinitely
    if event.type == 0:
        if event.code != 0:
            log("0-" + str(event.code) + "-" + str(event.value))
    elif event.type == 3:            
        if event.code == 0:
            if event.value < LeftCenterXMin or event.value > LeftCenterXMax:
                # log ("0[Left/X] " + str(event.value))
                LeftXMax = max(LeftXMax, event.value)
                LeftXMin = min(LeftXMin, event.value)
        elif event.code == 1:
            if event.value < LeftCenterYMin or event.value > LeftCenterYMax:
                # log ("1[Left/Y] " + str(event.value))
                LeftYMax = max(LeftYMax, event.value)
                LeftYMin = min(LeftYMin, event.value)
        elif event.code == 3:
            if event.value < RightCenterXMin or event.value > RightCenterXMax:
                # log ("3[Right/X] " + str(event.value))
                RightXMax = max(RightXMax, event.value)
                RightXMin = min(RightXMin, event.value)
        elif event.code == 4:
            if event.value < RightCenterYMin or event.value > RightCenterYMax:
                # log ("4[Right/Y] " + str(event.value))
                RightYMax = max(RightYMax, event.value)
                RightYMin = min(RightYMin, event.value)
        else:
            log("1-" + str(event.code) + "-" + str(event.value))

    elif event.type == 1:
        log("1-" + str(event.code) + "-" + str(event.value))
        if event.code == 316:
            log("Home Pressed - Exiting")
            break

        if event.code == 315:
            speed = min(speed + 10, speedMax)
            log("speed: " + str(speed)) 

        if event.code == 314:
            speed = max(speed - 10, speedMin)
            log("speed: " + str(speed)) 

        if event.code == 311:
            running = event.value == 1
            backward = False
            log("running: " + str(running))

        if event.code == 310:
            running = event.value == 1
            backward = True
            log("running: " + str(running))

    else:
        log(str(event.type) + "-" + str(event.code) + "-" + str(event.value))

log("Left Y: " + str(LeftYMin) + " - " + str(LeftYMax))
log("Left X: " + str(LeftXMin) + " - " + str(LeftXMax))
log("Right Y: " + str(RightYMin) + " - " + str(RightYMax))
log("Right X: " + str(RightXMin) + " - " + str(RightXMax))