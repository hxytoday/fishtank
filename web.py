# -*-coding: utf-8 -*-
# @Time : 2021-01-04 11:14
# @Author : hxy
# @FileName : web.py
# @Software : PyCharm
# @Email : 976396706@qq.com
# ---------------------------------
# web页面解析
#
# ----------------------------------
import socket
import time
from screen import display
from cue import lamp, music
from control import light
from config import read_conf
from sensor import temp_get

def httpserver(wlan):
    addr = (wlan.ifconfig()[0], 80)
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    display('server start')
    while True:
        c, caddr = s.accept()
        c_file = c.makefile('rwb', 0)  # 返回与socket对象关联的文件对象。rwb:支持二进制模式的读写操作 0:默认值，不支持缓存
        req = b''

        while True:
            line = c_file.readline()  # 逐行读取文件
            if not line or line == b'\r\n':
                break
            req += line
        time.sleep_ms(10)
        print("Request:")
        req = req.decode('utf-8').split('\r\n')  # 解码并分割字符
        req_data = req[0].lstrip().rstrip().replace(' ', '').lower()  # 列表第一行去头去尾转换小写
        if req_data.find('favicon.ico') > -1:
            c.close()
            continue
        else:
            req_data = req_data.replace('get/?', '').replace('http/1.1', '')
            index = req_data.find('key=')
            value = req_data[index + 4:].lstrip().rstrip()
            print('key:', value)
            if value == 'PumpOn':
                display('Pump on')
                lamp(2)
                music('Xxx')
            elif value == 'PumpOff':
                display('pump off')
                music('Dh')
                lamp(2)
            elif value == 'warm_on':
                display('warm on')
                lamp(2)
                light('r')
            elif value == 'warm_off':
                display('warm off')
                lamp(2)
                light('g')
            elif value == 'fog_on':
                display('fog on')
                lamp(2)
            elif value == 'fog_off':
                display('fog off')
                lamp(2)
            elif value == 'valve_on':
                display('valveon on')
                lamp(2)
            elif value == 'valve_off':
                display('valveon off')
                lamp(2)
            elif value == 'light_on':
                display('light on')
                lamp(2)
            elif value == 'light_off':
                display('light off')
                lamp(2)
            else:
                display(value)
                lamp(5)

        with open("control.html", 'r')as f:

            for line in f:
                if 'WaterTemp' in line:
                    line = line.replace('WaterTemp', read_conf('WaterTemp'))
                elif 'HwaterTemp' in line:
                    line = line.replace('HwaterTemp', read_conf('HTemp'))
                elif 'IndoorTemp' in line:
                    line = line.replace('IndoorTemp', read_conf('AirTemp'))
                elif 'Hum' in line:
                    line = line.replace('Hum', read_conf('Hum'))
                elif 'PumpState' in line:
                    line = line.replace('PumpState', '开')
                elif 'WarmState' in line:
                    line = line.replace('WarmState', '开')
                elif 'FogState' in line:
                    line = line.replace('FogState', 'on')
                elif 'ValveonState' in line:
                    line = line.replace('ValveonState', 'off')
                elif 'LightState' in line:
                    line = line.replace('LightState', 'off')
                c.send(line)

        c.close()

