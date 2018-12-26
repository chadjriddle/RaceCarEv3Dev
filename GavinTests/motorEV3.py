#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_D, OUTPUT_A
from ev3dev2.motor import MediumMotor, OUTPUT_B
from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep


lmA = LargeMotor(OUTPUT_A)
lmD = LargeMotor(OUTPUT_D)
SmB = MediumMotor(OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_D, OUTPUT_A)
steer_pair.on_for_rotations(0,SpeedRPS(2),3)
SmB.on_for_seconds(SpeedRPS(1),1)
steer_pair.on_for_rotations(0,SpeedRPS(2),3)
SmB.on_for_seconds(SpeedRPS(-1),1)