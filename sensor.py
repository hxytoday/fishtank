import dht
import ds18x20
import onewire
from machine import Pin, Timer
from config import param_data

ow = onewire.OneWire(Pin(4))
ds = ds18x20.DS18X20(ow)
rom = ds.scan()
d = dht.DHT11(Pin(27))


def temp_get(tim):
    ds.convert_temp()
    tem = str('%.1f' % ds.read_temp(rom[0]))
    d.measure()
    airtem = str(d.temperature())
    hum = str(d.humidity())
    param_data["WaterTemp"] = tem
    param_data["AirTemp"] = airtem
    param_data["Hum"] = hum
    param_data["HTemp"] = '99'


def update_sensor():
    tim = Timer(-1)
    tim.init(period=10000, mode=Timer.PERIODIC, callback=temp_get)
