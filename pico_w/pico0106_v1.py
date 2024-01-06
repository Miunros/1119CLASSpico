import network
import time
# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('NancyHsu', '22222222')

#處以正在連線vvvvvvvvvvvvv
max_wait=10 #建立變數
while max_wait>0: #比較變數
    max_wait -=1  #每秒相減1，直到max_wait<=0才會跳出
    status = nic.status()
    if status >=3 or status <0: #大於等於3表示錯誤訊息；<0表示沒有主機
        break
    print("等待連線中")
    time.sleep(1)

#可能完全沒有連線(沒有wifi機)
if nic.status() != 3:
    #開發狀態底下不使用重新開機的功能wdt = WDT(timeout=2000)
    #實際產品化再重新開機wdt.feed()
    raise RuntimeError('連線失敗')

else:
    print("連線成功")
    print (nic.ifconfig())
