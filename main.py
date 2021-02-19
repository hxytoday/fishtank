import _thread
import time
from machine import Pin, RTC, WDT
from sensor import update_sensor
from wireless import wifi_connect

wdt = WDT(timeout=2000)
rtc = RTC()
KEY = Pin(0, Pin.IN, Pin.PULL_UP)


def fun(KEY):
    time.sleep_ms(10)
    if KEY.value() == 0:
        datetime = rtc.datetime()
        print('Time is ', datetime)


KEY.irq(fun, Pin.IRQ_FALLING)


def fed_dog():
    while True:
        time.sleep_ms(1500)
        wdt.feed()


_thread.start_new_thread(fed_dog, ())
_thread.start_new_thread(update_sensor, ())
_thread.start_new_thread(wifi_connect, ())
