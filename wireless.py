"""
名称：连接无线路由器
说明：编程实现连接路由器，将IP地址等相关信息通过OLED显示（只支持2.4G网络）。
"""
import network
import time
from cue import lamp, beep, music
from screen import display
from web import httpserver
from boot import param_data
import socket
import ntptime
from config import sava_all_file

# 网络校时
def sync_ntp():
    ntptime.NTP_DELTA = 3155644800  # 可选 UTC+8偏移时间（秒），不设置就是UTC0
    ntptime.host = 'ntp1.aliyun.com'  # 可选，ntp服务器，默认是"pool.ntp.org"
    ntptime.settime()  # 修改设备时间,到这就已经设置好了


# WIFI连接函数
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)  # STA模式
    wlan.active(True)  # 激活接口
    start_time = time.time()  # 记录时间做超时判断
    if not wlan.isconnected():
        print('connecting to network...')
        ssid = param_data.get('ssid')  # 读取WiFi账号密码
        passwd = param_data.get('password')
        print('ssid is %s , password is %s' % (ssid, passwd))
        wlan.connect(ssid, passwd)
        while not wlan.isconnected():
            # LED闪烁提示
            # lamp(2)
            # beep(400, 500)
            # 超时判断,15秒没连接成功判定为超时
            if time.time() - start_time > 10:
                print('WIFI Connected Timeout!')
                break
        if not wlan.isconnected():
            wlan.active(False)
            do_ap()
    if wlan.isconnected():
        # LED点亮
        lamp('on')
        beep(1000, 500)
        # 串口打印信息
        print('network information:', wlan.ifconfig())
        # OLED数据显示
        display(wlan.ifconfig()[0])
        sync_ntp()
        httpserver(wlan)


def do_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='test', authmode=0)
    print('AP is up')
    addr = ('192.168.4.1', 80)
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    display('AP  start')
    while True:
        c, caddr = s.accept()
        c_file = c.makefile('rwb', 0)  # 返回与socket对象关联的文件对象。rwb:支持二进制模式的读写操作 0:默认值，不支持缓存
        req = b''  # 定义bytes类型字符串
        print('AP server start')

        while True:
            line = c_file.readline()  # 逐行读取文件
            if not line or line == b'\r\n':
                break
            req += line
        # time.sleep_ms(10)
        print("Request:")
        req = req.decode('utf-8').split('\r\n')  # 解码并分割字符
        req_data = req[0].lstrip().rstrip().replace(' ', '').lower()  # 列表第一个元素去除空格转换小写

        if req_data.find('favicon.ico') > -1:
            c.close()
            continue
        else:
            req_data = req_data.replace('get/?', '').replace('http/1.1', '')
            index = req_data.find('ssid')
            if index > -1:
                req_data = req_data.split('&')
                for i in range(len(req_data)):
                    data = req_data[i].split('=')
                    param_data[data[0]] = data[1]

                print('req_data is:', param_data)
                sava_all_file()

        with open("set.html", 'r')as f:

            for line in f:
                if 'user_data1' in line:
                    data = param_data.get('ssid')
                    line = line.replace('user_data1', str(data))
                elif 'user_data2' in line:
                    data = param_data.get('password')
                    line = line.replace('user_data2', str(data))
                c.send(line.encode())

        c.close()
