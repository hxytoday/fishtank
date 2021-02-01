import _thread
import time

from machine import Pin, RTC
from cue import music
from sensor import update_sensor
from wireless import wifi_connect

rtc = RTC()
KEY = Pin(0, Pin.IN, Pin.PULL_UP)


def fun(KEY):
    time.sleep_ms(10)
    if KEY.value() == 0:
        _thread.start_new_thread(music, ('Xxx',))
        datetime = rtc.datetime()
        print('Time is ', datetime)


KEY.irq(fun, Pin.IRQ_FALLING)

_thread.start_new_thread(update_sensor, ())
_thread.start_new_thread(wifi_connect, ())
