from machine import Timer, WDT, ADC
import network
import time
import urequests as requests

def connect():
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

def mycallback(t):
    print('Hello World!')
    t.deinit()

def alert():
    print('要爆炸了!!!')
    res = requests.get(url='https://hook.us1.make.com/tw20asr31id34dhmjlaf1usu162hw758')
    print(help(response))
    response.close()
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 26 and delta >= 60 * 1000:        
        alert()
        start = time.ticks_ms()#重新設定計時的時間

connect()
start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒
time1 = Timer()
time1.init(period=1000,callback=callback1)

#https://hook.us1.make.com/tw20asr31id34dhmjlaf1usu162hw758


