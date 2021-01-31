from wireless import wifi_connect
from sensor import update_sensor
from machine import Pin
import time
from cue import music
import _thread

KEY = Pin(0, Pin.IN, Pin.PULL_UP)


def fun(KEY):
    time.sleep_ms(10)
    if KEY.value() == 0:
        music('Xxx')
        print('KEY is hold')


KEY.irq(fun, Pin.IRQ_FALLING)

def hi():
    while True:
        print('i m test one')
        time.sleep(10)


_thread.start_new_thread(update_sensor, ())
_thread.start_new_thread(wifi_connect, ())
# _thread.start_new_thread(hi, ())
