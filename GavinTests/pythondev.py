#!/usr/bin/env python3
#importing from libraries
from sys import stderr
from ev3dev2.button import Button
from ev3dev2.led import Leds
logf = open("process.log", "w")

def log(message):
    logf.write(message + "\n")
    logf.flush()
    print(message)

log("gavin is cool")
#defining abreviation
#dad: creating and Instance of the Button class and assigning the instance to the btn variable
btn = Button()
leds = Leds()
# setting LED's off
leds.all_off()
print("hello world", file=stderr)

while True:
   
    #if the button is up dont do anything
    #dad: what does the keyword "break" do?
    if btn.up:
        break
    #if the right button is pressed change the collor to amber
    elif btn.right:
        leds.set_color('RIGHT', 'AMBER')
    #if the left button is pressed change color to green
    elif btn.left:
        leds.set_color('LEFT', 'GREEN')