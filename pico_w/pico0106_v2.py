from tools import connect, reconnect 
from machine import Timer, WDT, ADC,RTC
import network
import time
import urequests as requests


def mycallback(t):
    print('Hello World!')
    t.deinit()

def alert(t:float):
    print('要爆炸了!!!')
    rtc= RTC()
    date_time=rtc.datetime()
    year = date_time[0]
    month = date_time[1]
    day = date_time[2]
    hour = date_time[4]
    minites = date_time[5]
    second = date_time[6]
    date_str=f'{year}-{month}-{day}-{hour}:{minites}:{second}'
    try:
        res = requests.get(f'https://hook.us1.make.com/tw20asr31id34dhmjlaf1usu162hw758?name=台北&date={date_str}&temperature={t}&place=Taipei')
    except:
        reconnect()        
    else:
        if reconnect.status_code==200:
            print('傳送成功')
        else:
            print('Server有錯誤訊息')
            print(f'status_code:{response.status_code}')
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
    if temperature >= 25 and delta >= 60 * 1000:        
        alert(temperature)
        start = time.ticks_ms()#重新設定計時的時間

connect()
start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒
time1 = Timer()
time1.init(period=1000,callback=callback1)

#https://hook.us1.make.com/tw20asr31id34dhmjlaf1usu162hw758


