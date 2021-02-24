from machine import *
from utime import sleep, ticks_ms
from urandom import randint

# setup()
## Dig. 1~4
DIG = (Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT))
## Seg. a~g
SEG = (Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(6, Pin.OUT),
       Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT), Pin(10, Pin.OUT))
## Seg. dp
SEG_DP = Pin(11, Pin.OUT)

BUTTON = Pin(14, Pin.IN)
SPEAKER  = Pin(16, Pin.OUT)

SEG_CHARS = {
    ' ': (0,0,0,0,0,0,0),
    '0': (1,1,1,1,1,1,0),
    '1': (0,1,1,0,0,0,0),
    '2': (1,1,0,1,1,0,1),
    '3': (1,1,1,1,0,0,1),
    '4': (0,1,1,0,0,1,1),
    '5': (1,0,1,1,0,1,1),
    '6': (1,0,1,1,1,1,1),
    '7': (1,1,1,0,0,0,0),
    '8': (1,1,1,1,1,1,1),
    '9': (1,1,1,1,0,1,1),
    'E': (1,0,0,1,1,1,1)
}

def clear_all_dig():
    for i in DIG: i.off()
def clear_all_seg():
    for i in SEG: i.on()
    SEG_DP.on()

def show_char(char, digit, interval=0.00025, dp=False):
    clear_all_dig();clear_all_seg()
    DIG[digit-1].on()
    for ind, i in enumerate(SEG_CHARS[char]):
        if i == 1:
            SEG[ind].off()
        else:
            SEG[ind].on()
    if dp:
        SEG_DP.off()
    sleep(interval)

def show_number(num, zero_padding=False):
    n = list(num)
    if not zero_padding:
        n = list('{:>4}'.format(num))
    for i in range(4):
        show_char(n[i], i+1, dp=(i==1))

# main()
cnt = 0
s = ticks_ms()
while True:
    sec = (ticks_ms()-s)//1000
    show_number('%02d%02d'%(sec//60, sec%60))