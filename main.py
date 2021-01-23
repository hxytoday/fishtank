from wireless import wifi_connect
from sensor import update_sensor
from machine import Pin
import time
from cue import music
from control import servo

KEY = Pin(0, Pin.IN, Pin.PULL_UP)
servo(90)

def fun(KEY):
    time.sleep_ms(10)
    if KEY.value() == 0:
        music('Xxx')
        print('KEY is hold')


KEY.irq(fun, Pin.IRQ_FALLING)

update_sensor()
time.sleep(10)
wifi_connect()
