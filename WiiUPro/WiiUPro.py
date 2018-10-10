#!/usr/bin/env python3

import evdev
import ev3dev.auto as ev3
import threading

class WiiUPro():

    BUTTON_TYPE = 1
    AXIS_TYPE = 3

    X_BUTTON = 307
    A_BUTTON = 305
    B_BUTTON = 304
    Y_BUTTON = 308
    PLUS_BUTTON = 315
    MINUS_BUTTON = 314
    HOME_BUTTON = 316
    RIGHT_STICK_BUTTON = 318
    LEFT_STICK_BUTTON = 317
    DPAD_UP_BUTTON = 544
    DPAD_RIGHT_BUTTON = 547
    DPAD_DOWN_BUTTON = 545
    DPAD_LEFT_BUTTON = 546
    ZR_BUTTON = 313
    ZL_BUTTON = 312
    R_BUTTON = 311
    L_BUTTON = 310

    LEFT_X_AXIS = 0
    LEFT_Y_AXIS = 1
    RIGHT_X_AXIS = 3
    RIGHT_Y_AXIS = 4

    values = {
        X_BUTTON: 0,
        A_BUTTON: 0,
        B_BUTTON: 0,
        Y_BUTTON: 0,
        PLUS_BUTTON: 0,
        MINUS_BUTTON: 0,
        HOME_BUTTON: 0,
        RIGHT_STICK_BUTTON: 0,
        LEFT_STICK_BUTTON: 0,
        DPAD_UP_BUTTON: 0,
        DPAD_RIGHT_BUTTON: 0,
        DPAD_DOWN_BUTTON: 0,
        DPAD_LEFT_BUTTON: 0,
        ZR_BUTTON: 0,
        ZL_BUTTON: 0,
        R_BUTTON: 0,
        L_BUTTON: 0,
        LEFT_X_AXIS: 0,
        LEFT_Y_AXIS: 0,
        RIGHT_X_AXIS: 0,
        RIGHT_Y_AXIS: 0
    }

    wiiUProDev = None
    logFunc = None
    gamepad = None

    def Setup(self, logFunc):
        self.logFunc = logFunc

    def Connect(self):
        self.__log__("Finding WiiU Pro controller...")
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            if device.name == 'Nintendo Wii Remote Pro Controller':
                self.wiiUProDev = device.fn
        if self.wiiUProDev:
             self.__log__("Controller Found!")
             self.gamepad = evdev.InputDevice(wiiUProDev)
             return True
        else:
             self.__log__("Controller NOT Found!")
             return False

    def __log__(self, message):
        if self.logFunc != None:
            self.logFunc(message)

    def MainLoop(self):
        if self.gamepad == None:
            self.__log__("No Gamepad Available")
            return
        for event in self.gamepad.read_loop():   #this loops infinitely
            if event.type == 0:
                if event.code != 0:
                    self.__log__("0-" + str(event.code) + "-" + str(event.value))
            elif event.type == self.AXIS_TYPE:            
                self.values[event.code] = event.value

            elif event.type == self.BUTTON_TYPE:
                self.values[event.code] = event.value

            else:
                self.__log__(str(event.type) + "-" + str(event.code) + "-" + str(event.value))