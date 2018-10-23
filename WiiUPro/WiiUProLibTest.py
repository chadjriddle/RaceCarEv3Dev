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
controller.Start()

while True:
    if controller.Home:
        break
    if controller.A:
        Log("A Pressed")
        break
    if controller.B:
        Log("B Pressed")
        break


controller.Stop()