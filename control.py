from machine import Pin
from neopixel import NeoPixel
import random
import time


pin = Pin(22, Pin.OUT)
np = NeoPixel(pin, 30)


def color_buf(mode, delay=0):
    if mode == 'on':

        for i in range(30):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            np[i] = (r, g, b)
            time.sleep_ms(delay)
            np.write()
    elif mode == 'off':
        for i in range(30):
            np[i] = (0, 0, 0)


def light(mode):  # on off
    if mode == 'on':
        color_buf(mode,200)
    else:
        color_buf(mode)

    np.write()
