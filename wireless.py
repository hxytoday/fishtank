"""
名称：连接无线路由器
说明：编程实现连接路由器，将IP地址等相关信息通过OLED显示（只支持2.4G网络）。
"""
import network
import time
from config import read_conf
from control import light
from cue import lamp, beep, music
from screen import display
from web import httpserver

# WIFI连接函数
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)  # STA模式
    wlan.active(True)  # 激活接口
    start_time = time.time()  # 记录时间做超时判断
    if not wlan.isconnected():
        print('connecting to network...')
        ssid = read_conf('ssid')  # 读取WiFi账号密码
        passwd = read_conf('password')
        print('ssid is %s , password is %s' % (ssid, passwd))
        wlan.connect(ssid, passwd)
        while not wlan.isconnected():
            # LED闪烁提示
            lamp(2)
            beep(400, 500)
            # 超时判断,15秒没连接成功判定为超时
            if time.time() - start_time > 15:
                print('WIFI Connected Timeout!')
                break
    if wlan.isconnected():
        # LED点亮
        lamp('on')
        beep(1000, 500)
        # 串口打印信息
        print('network information:', wlan.ifconfig())
        # OLED数据显示
        display(wlan.ifconfig()[0])
        httpserver(wlan)



