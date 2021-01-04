from machine import Pin
import time,dht,ujson
from wireless import WIFI_Connect
from screen import display

f=open("config.json","r")   #读取配置文件WiFi信息
data=ujson.loads(f.read())
f.close()
ssid=data["ssid"]
passwd=data["password"]
display(ssid)
WIFI_Connect(ssid,passwd)

# cpu_tem=esp32.raw_temperature()
# led=Pin(2,Pin.OUT,value=1)


# oled.text("CPU_Temp "+str((cpu_tem-32)/1.8),  0, 20)      #写入第2行内容
# #oled.text("led",  0, 50)      #写入第3行内容

# d = dht.DHT11(Pin(27))
# d.measure()
#
# while True:
#     time.sleep(1)
#     led.value(not led.value())
#     print(led.value())
#     state=led.value()
#     oled.text(str(d.temperature() )+' C',0,40)   #温度显示
#     oled.text(str(d.humidity())+' %',48,40)  #湿度显示
#     oled.show()

