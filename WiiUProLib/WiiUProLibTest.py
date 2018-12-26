#!/usr/bin/env python3
import sys
from WiiUPro import WiiUPro

logf = open("process.log", "w")

def log(message):
    logf.write(message + "\n")
    logf.flush()
    print(message, file=sys.stderr)

log("starting...")

controller = WiiUPro()

controller.Setup(log)
controller.Connect()
controller.Start()

while True:
    if controller.Home:
        break
    if controller.A == WiiUPro.PRESSED:
        log("A Pressed")
    if controller.DP_Down == WiiUPro.PRESSED:
        log("DP_Down Pressed")
    if controller.B == WiiUPro.RELEASED:
        log("B Released")


log("stopping....")
controller.Stop()