'''
实验名称：连接无线路由器
版本：v1.0
日期：2019.8
作者：01Studio
说明：编程实现连接路由器，将IP地址等相关信息通过OLED显示（只支持2.4G网络）。
'''
import network, time
from screen import display
import socket
from led import lamp, beep, music
from control import lig


# WIFI连接函数
def WIFI_Connect(ssid, passwd):
    wlan = network.WLAN(network.STA_IF)  # STA模式
    wlan.active(True)  # 激活接口
    start_time = time.time()  # 记录时间做超时判断

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, passwd)  # 输入WIFI账号密码

        while not wlan.isconnected():

            # LED闪烁提示
            lamp(4)
            # beep(400,500)

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


def httpserver(wlan):
    addr = (wlan.ifconfig()[0], 80)
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    display('s')
    while True:
        c, caddr = s.accept()
        c_file = c.makefile('rwb', 0)  # 返回与socket对象关联的文件对象。rwb:支持二进制模式的读写操作 0:默认值，不支持缓存
        req = b''
        while True:
            line = c_file.readline()  # 逐行读取文件
            if not line or line == b'\r\n':
                break
            req += line

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
                lig('r')
            elif value == 'warm_off':
                display('warm off')
                lamp(2)
                lig('g')
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
                    line = line.replace('WaterTemp', '32.5')
                elif 'HwaterTemp' in line:
                    line = line.replace('HwaterTemp', '42')
                elif 'IndoorTemp' in line:
                    line = line.replace('IndoorTemp', '16')
                elif 'Hum' in line:
                    line = line.replace('Hum', '34')
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
