#!/usr/bin/env python3

from WiiUPro import WiiUPro

logf = open("process.log", "w")

def log(message):
    logf.write(message + "\n")
    logf.flush()
    print(message)

log("starting...")

controller = WiiUPro()

controller.Setup(log)
controller.Connect()

while True:
    controller.MainLoop()
    if controller.HOME_BUTTON:
        break