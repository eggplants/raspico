from machine import *
from utime import sleep

sense_temp = ADC(4)

def volt_to_temp(value: float) -> float:
    reading = value * 3.3 /65535
    temp = 27 - (reading - 0.706) / 0.001721
    return temp

while True:
    now_digital = sense_temp.read_u16()
    print(volt_to_temp(now_digital), end='\r')
    sleep(1)