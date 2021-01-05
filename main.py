from wireless import wifi_connect
from screen import display
import time
from sersor import update_sersor

display('hi there')
update_sersor()
time.sleep(3)

wifi_connect()



