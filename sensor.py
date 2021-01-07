from machine import Pin, Timer
import onewire, ds18x20, dht, time
from config import write_conf
from screen import display

ow = onewire.OneWire(Pin(4))
ds = ds18x20.DS18X20(ow)
rom = ds.scan()
d = dht.DHT11(Pin(27))


def temp_get(tim):
    ds.convert_temp()
    tem = str('%.1f'%ds.read_temp(rom[0]))
    write_conf('WaterTemp', tem)
    d.measure()
    airtem = str(d.temperature())
    hum = str(d.humidity())
    write_conf('AirTemp', airtem)
    write_conf('Hum', hum)


def update_sensor():
    tim = Timer(-1)
    tim.init(period=10000, mode=Timer.PERIODIC, callback=temp_get)
