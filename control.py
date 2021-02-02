from machine import Pin, PWM
from neopixel import NeoPixel
import random
import time
from boot import param_data

pin = Pin(22, Pin.OUT)
np = NeoPixel(pin, 30)
s1 = PWM(Pin(18), freq=50, duty=0)
autoflag = param_data.get('autoflay')

'''
自动参数
水泵延时valuedelay
抽水时间valuetime
抽水间隔valueinterval
喷雾延时fogdelay
加热温度

'''


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
        color_buf(mode, 200)
    else:
        color_buf(mode)
    np.write()


def servo(angle):
    s1.duty(int(((angle + 90) * 2 / 180 + 0.5) / 20 * 1023))


start_time = time.time()


def auto():
    global start_time
    while autoflag == 1:
        if start_time / valuedelay == 0:
            pass
