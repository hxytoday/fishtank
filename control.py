from machine import Pin, PWM
from neopixel import NeoPixel
import random
import time
from config import param_data

pin = Pin(22, Pin.OUT)
np = NeoPixel(pin, 30)
s1 = PWM(Pin(18), freq=50, duty=0)
value = Pin(11, Pin.OUT)
autoflag = param_data.get('autoflay')
value_time = param_data.get('valuetime')
value_delay = param_data.get('valuedelay')
water_level = param_data.get('WaterLevel')
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


def value_run():
    if water_level < 4000:
        value.value(1)
    else:
        value.value(0)



def value_stop():
    value.value(0)

def fog_run():    #开启雾化器并触发电磁阀和灯光
    pass

def auto():
    i = 0
    now_time = time.time()
    while autoflag == 1:  # 自动模式下各设备的定时及延时运行
        if water_level >1000:
            fog_run()
        while i <= value_time:
            value_run()
            i = time.time() - now_time
            if i == value_time:
                now_time = time.time()
                i = 0
                break

        while i < value_delay:
            value_stop()
            i = time.time() - now_time
            if i == value_time:
                now_time = time.time()
                i = 0
                break

    while autoflag == 0:  # 非自动模式下各设备的控制以及保护
        pass
