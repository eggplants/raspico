from machine import *
from utime import sleep
BUTTON = Pin(14, Pin.IN)
SPEAKER = PWM(Pin(15, Pin.OUT))

# https://qiita.com/undo0530/items/7ce2ccc806668d911525
A4 = 440
B4 = 493.883
C5 = 523.251
C5s= 554.365
D5 = 587.330
E5 = 659.255
F5 = 698.456
F5s= 739.989
G5 = 783.991
A5 = 880
B5 = 987.767
C6 = 1046.502
MUSIC =  [D5,E5,0,D5,E5,0,G5,F5s,0,D5,E5,0,D5,E5,0,D5,E5,0,C6,B5,0,G5,A5,0,D5,E5,0,D5,E5,0,G5,F5s,0,D5,E5,0,B4,A4,0,B4,C5,0,C5s,D5,0,0,D5,0,D5,E5,0,D5,E5,0,G5,F5s,0,D5,E5,0,D5,E5,0,D5,E5,0,C6,B5,0,G5,A5,0,D5,E5,0,D5,E5,0,G5,F5s,0,D5,E5,0,B4,A4,A4,A4,A4,A4,A4,A4,A4,A4,0,0,F5,E5,0,E5,F5s,E5,F5s,G5,G5,G5,D5,0,B4,C5,0,C5,D5,C5s,D5,B4,B4,B4,0,0,D5,E5,0,D5,E5,0,G5,F5s,0,D5,E5,0,D5,E5,0,D5,E5,0,G5,F5s,0,D5,E5,0,D5,E5,0,D5,E5,0,C6,B5,0,0,G5,0,0,0,0,0,0,0,0,0,0,0,0,0,D5,E5,0,D5,E5,0,C6,B5,0,0,G5]

cnt = 0
while True:
    if cnt%len(MUSIC)==1:
        SPEAKER.duty_u16(0)
        sleep(2)
    elif BUTTON.value() == 0:
        f = int(MUSIC[cnt%len(MUSIC)] + 0.5)
        if f == 0:
            SPEAKER.duty_u16(0)
        else:
            SPEAKER.freq(f)
            SPEAKER.duty_u16(0x8000)
    else:
        SPEAKER.duty_u16(0)
    cnt += 1
    sleep(0.156)