from config import load_file
from machine import Pin
from wireless import do_ap
import time

param_data = {}
param_data = load_file()
KEY = Pin(0, Pin.IN, Pin.PULL_UP)

if KEY.value() == 0:
    time.sleep_ms(10)
    if KEY.value() == 0:
        do_ap()
