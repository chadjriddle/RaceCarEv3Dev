#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.led import Leds

btn = Button()
leds = Leds()

leds.all_off()


while True:
    if btn.up:
        break
    elif btn.right:
        leds.set_color('LEFT', 'AMBER')
    elif btn.left:
        leds.set_color('LEFT', 'GREEN')

leds.all_off()
sleep(1000)
print("Turning Off")