from wireless import wifi_connect
from sensor import update_sensor
import time
update_sensor()
time.sleep(1)
wifi_connect()
