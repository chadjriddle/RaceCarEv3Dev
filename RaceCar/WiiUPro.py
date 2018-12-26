#!/usr/bin/env python3

import evdev
import ev3dev.auto as ev3
import threading

class WiiUPro():

    UP = 0
    PRESSED = 1
    DOWN = 2
    RELEASED = 3


    __BUTTON_TYPE = 1
    __AXIS_TYPE = 3

    __X_BUTTON = 307
    __A_BUTTON = 305
    __B_BUTTON = 304
    __Y_BUTTON = 308
    __PLUS_BUTTON = 315
    __MINUS_BUTTON = 314
    __HOME_BUTTON = 316
    __RIGHT_STICK_BUTTON = 318
    __LEFT_STICK_BUTTON = 317
    __DPAD_UP_BUTTON = 544
    __DPAD_RIGHT_BUTTON = 547
    __DPAD_DOWN_BUTTON = 545
    __DPAD_LEFT_BUTTON = 546
    __ZR_BUTTON = 313
    __ZL_BUTTON = 312
    __R_BUTTON = 311
    __L_BUTTON = 310

    __LEFT_X_AXIS = 0
    __LEFT_Y_AXIS = 1
    __RIGHT_X_AXIS = 3
    __RIGHT_Y_AXIS = 4

    __values = {
        __X_BUTTON: 0,
        __A_BUTTON: 0,
        __B_BUTTON: 0,
        __Y_BUTTON: 0,
        __PLUS_BUTTON: 0,
        __MINUS_BUTTON: 0,
        __HOME_BUTTON: 0,
        __RIGHT_STICK_BUTTON: 0,
        __LEFT_STICK_BUTTON: 0,
        __DPAD_UP_BUTTON: 0,
        __DPAD_RIGHT_BUTTON: 0,
        __DPAD_DOWN_BUTTON: 0,
        __DPAD_LEFT_BUTTON: 0,
        __ZR_BUTTON: 0,
        __ZL_BUTTON: 0,
        __R_BUTTON: 0,
        __L_BUTTON: 0,
        __LEFT_X_AXIS: 0,
        __LEFT_Y_AXIS: 0,
        __RIGHT_X_AXIS: 0,
        __RIGHT_Y_AXIS: 0
    }

    __wiiUProDev = None
    __logFunc = None
    __gamepad = None
    __running = False

    def Setup(self, logFunc):
        self.__logFunc = logFunc

    def Connect(self):
        self.__log("Finding WiiU Pro controller...")
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            if device.name == 'Nintendo Wii Remote Pro Controller':
                self.__wiiUProDev = device.fn
        if self.__wiiUProDev:
             self.__log("Controller Found!")
             self.__gamepad = evdev.InputDevice(self.__wiiUProDev)
             return True
        else:
             self.__log("Controller NOT Found!")
             return False

    def Start(self):
        threading.Thread(target=self.__mainLoop).start()

    def Stop(self):
        self.__running = False

    @property
    def IsRunning(self):
        return self.__running
    
    @property
    def Home(self):
        return self.__readButtonState(self.__HOME_BUTTON)
    
    @property
    def Minus(self):
        return self.__readButtonState(self.__MINUS_BUTTON)

    @property
    def Plus(self):
        return self.__readButtonState(self.__PLUS_BUTTON)

    @property
    def A(self):
        return self.__readButtonState(self.__A_BUTTON)

    @property
    def B(self):
        return self.__readButtonState(self.__B_BUTTON)

    @property
    def X(self):
        return self.__readButtonState(self.__X_BUTTON)

    @property
    def Y(self):
        return self.__readButtonState(self.__Y_BUTTON)

    @property
    def R_Stick(self):
        return self.__readButtonState(self.__RIGHT_STICK_BUTTON)

    @property
    def L_Stick(self):
        return self.__readButtonState(self.__LEFT_STICK_BUTTON)

    @property
    def DP_Up(self):
        return self.__readButtonState(self.__DPAD_UP_BUTTON)

    @property
    def DP_Down(self):
        return self.__readButtonState(self.__DPAD_DOWN_BUTTON)

    @property
    def DP_Left(self):
        return self.__readButtonState(self.__DPAD_LEFT_BUTTON)

    @property
    def DP_Right(self):
        return self.__readButtonState(self.__DPAD_RIGHT_BUTTON)

    @property
    def ZR(self):
        return self.__readButtonState(self.__ZR_BUTTON)

    @property
    def ZL(self):
        return self.__readButtonState(self.__ZL_BUTTON)

    @property
    def RB(self):
        return self.__readButtonState(self.__R_BUTTON)

    @property
    def LB(self):
        return self.__readButtonState(self.__L_BUTTON)

    @property
    def LeftAxisY(self):
        return self.__values[self.__LEFT_Y_AXIS]

    @property
    def LeftAxisX(self):
        return self.__values[self.__LEFT_X_AXIS]

    @property
    def RightAxisY(self):
        return self.__values[self.__RIGHT_Y_AXIS]

    @property
    def RightAxisX(self):
        return self.__values[self.__RIGHT_X_AXIS]

    def __readButtonState(self, buttonId):
        if self.__values[buttonId] == self.PRESSED:
            self.__values[buttonId] = self.DOWN
            return self.PRESSED
        elif self.__values[buttonId] == self.RELEASED:
            self.__values[buttonId] = self.UP
            return self.RELEASED
        elif self.__values[buttonId] == self.DOWN:
            return self.DOWN
        else:
            return self.UP


    def __log(self, message):
        if self.__logFunc != None:
            self.__logFunc(message)

    def __mainLoop(self):
        self.__running = True
        if self.__gamepad is None:
            self.__log("No Gamepad Available")
            self.__running = False
            return

        for event in self.__gamepad.read_loop():
            if self.__running == False:
                break

            #self.__resetReleased()

            if event.type == 0:
                if event.code != 0:
                    self.__log("Unhandled Event: 0-" + str(event.code) + "-" + str(event.value))
            elif event.type == self.__AXIS_TYPE:            
                self.__values[event.code] = event.value

            elif event.type == self.__BUTTON_TYPE:
                if event.value:
                    if self.__values[event.code] == self.UP or self.__values[event.code] == self.RELEASED:
                        self.__values[event.code] = self.PRESSED
                else:
                    if self.__values[event.code] == self.DOWN or self.__values[event.code] == self.PRESSED:
                        self.__values[event.code] = self.RELEASED


            else:
                self.__log("Unhandled Event: " + str(event.type) + "-" + str(event.code) + "-" + str(event.value))
        
        self.__log("Exiting Main Loop")

