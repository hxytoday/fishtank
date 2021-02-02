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
from screen import display
from cue import lamp
from cue import music
from control import light, servo
from boot import param_data


def httpserver(wlan):
    addr = (wlan.ifconfig()[0], 80)
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    display('server start')
    while True:
        c, caddr = s.accept()
        c_file = c.makefile('rwb', 0)  # 返回与socket对象关联的文件对象。rwb:支持二进制模式的读写操作 0:默认值，不支持缓存
        req = b''  # 定义bytes类型字符串
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

            index = req_data.find('key=')
            if index > -1:
                value = req_data[index + 4:].lstrip().rstrip()
                print('key:', value)
                if value == 'PumpOn':
                    display('Pump on')
                    servo(90)
                    lamp(2)
                elif value == 'PumpOff':
                    display('pump off')
                    servo(0)
                    lamp(2)
                elif value == 'warm_on':
                    display('warm on')
                    lamp(2)
                    music('Xxx')
                elif value == 'warm_off':
                    display('warm off')
                    lamp(2)
                    music('Dh')
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
                    light('on')
                elif value == 'light_off':
                    display('light off')
                    lamp(2)
                    light('off')
                else:
                    display(value)
                    lamp(5)
            else:
                index = req_data.find('fog')
                if index > -1:
                    req_data = req_data.split('&')
                    for i in range(len(req_data)):
                        data = req_data[i].split('=')
                        param_data[data[0]] = data[1]

                    print('req_data is:', param_data)

        with open("control.html", 'r')as f:

            for line in f:
                if 'WaterTemp' in line:
                    data = param_data.get('WaterTemp', '999')
                    line = line.replace('WaterTemp', data)
                elif 'HwaterTemp' in line:
                    data = param_data.get('HTemp', '999')
                    line = line.replace('HwaterTemp', data)
                elif 'IndoorTemp' in line:
                    data = param_data.get('AirTemp', '999')
                    line = line.replace('IndoorTemp', data)
                elif 'Hum' in line:
                    data = param_data.get('Hum', '999')
                    line = line.replace('Hum', data)
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
                c.send(line.encode())

        c.close()
