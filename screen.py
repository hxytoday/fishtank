# import time
from machine import I2C,Pin
from ssd1306 import SSD1306_I2C

#初始化相关模块
i2c = I2C(sda=Pin(13), scl=Pin(14))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

def display(data):
    oled.fill(0)  # 清屏背景黑色
    oled.text('life is color', 0, 0)
    oled.text(data, 0, 20)
    oled.show()
