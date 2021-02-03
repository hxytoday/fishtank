from machine import Pin
from wireless import do_ap
import time
from config import read_param

read_param()

# KEY = Pin(0, Pin.IN, Pin.PULL_UP)
#
# if KEY.value() == 1:
#     time.sleep_ms(200)
#     if KEY.value() == 1:
#         do_ap()
