from machine import Pin, Timer
from neopixel import NeoPixel

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pin = Pin(22, Pin.OUT)
np = NeoPixel(pin, 30)


def Color_buf(color):
    for i in range(30):
        np[i] = color


def lig(co):
    if co == 'r':
        Color_buf(RED)
        np.write()
    elif co == 'g':
        Color_buf(GREEN)
        np.write()
    else:
        Color_buf(BLUE)
        np.write()
