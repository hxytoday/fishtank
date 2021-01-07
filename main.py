from wireless import wifi_connect
from sensor import update_sersor
import time
update_sersor()
time.sleep(1)
wifi_connect()
