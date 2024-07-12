import machine
import time
import network
import urequests
import random


ssid = 'Wanglab_G'
password = 'wanglab666666'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
chipid = int.from_bytes(wlan.config('mac'), 'big') % 65536
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

while True:
    value = random.randint(0, 999) / 10
    url = "http://XXXXXXXX?chipid=RPI" + str(chipid) + "&val0=" + str(value)
    r = urequests.get(url)
    print(r.content)
    r.close()
    time.sleep(60)