Connecting the Wii U Pro Controller to Ev3Dev
(https://retropie.org.uk/docs/Wii-U-Pro-Controller/)

sudo bluetoothctl

power on
agent on
pairable on
<press red sync button>                                         # not a command press the button on the controller
scan on
pair <MAC of the found wiimote, use TAB for autocompletion>     # note: we do not explicitly connect, we just pair!
connect <MAC of the wiimote>                                    # there seems to be a pretty short timeout, so execute this immediately after the pairing command
trust <MAC of the wiimote>
disconnect <MAC of the wiimote>

Events:

Button Press - Type = 1 (Value: Pressed = 1 Released = 0)
    X Button - Code = 307
    A Button - Code = 305
    B Button - Code = 304
    Y Button - Code = 308
    + Button - Code = 315
    - Button - Code = 314
    Home Button - Code = 316
    Right Stick Button = 318
    Left Stick Button = 317

    DPAD Up - Code = 544
    DPAD Right - Code = 547
    DPAD Down - Code = 545
    DPAD Left - Code = 546

    ZR Button - Code = 313
    R Button - Code = 311
    L Button - Code = 310
    ZL Button - Code = 312

Power Button does not appear to be a Button of Type 1

