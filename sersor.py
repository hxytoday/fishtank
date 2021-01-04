from machine import Pin,I2C,Timer
import onewire,ds18x20,dht,time

ow=onewire.OneWire(Pin(4))
ds=ds18x20.DS18X20(ow)
rom=ds.scan()

def temp_get():
    ds.convert_temp()
    tem=ds.read_temp(rom[0])
    return tem

d=dht.DHT11(Pin(27))

def dht_get():
    d.measure()
    tem=d.temperature()
    hum=d.humidity()
    return tem,hum
