from machine import Timer, WDT, ADC,RTC
import network
import time
import urequests as requests

ssid = 'NancyHsu'
password='22222222'

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(ssid, password)
nic.config=(pm=0xa11140)

def connect():
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
def reconnect():
    if nic.status()==3:
        print('無法連線({nic.status()})')
        return
    else:
        print('嘗試重新連線')
        nic.disconnect()
        nic.connect(ssid, password)
        connect()