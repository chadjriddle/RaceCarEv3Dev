#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A
from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.button import Button
running = True
lmA = LargeMotor(OUTPUT_A)
btn = Button()
if btn.any(): 
    
if running = True:
    lmA.on(speed=50)
