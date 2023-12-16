from machine import ADC, Timer, Pin
import time

def alert():
    print('要爆炸了')
    
def callback1(t:Timer):
    global start
    sensor=ADC(4)
    vol=sensor.read_u16()*(3.3/65535)
    temp=27-(vol-0.706)/0.001721
    print(f'溫度:{temp}')
    delta = time.ticks_diff(time.ticks_ms(), start)
    #print(delta)
    #溫度如果超過24度每5秒會發一次通知
    led = Pin("LED", Pin.OUT)
    if temp >=24 and delta>=5*1000:
        alert()
        if temp >=24.5:
            led.high()
            time.sleep_ms(500)
            led.low()
            time.sleep(1)
        start = time.ticks_ms()#重新設定計時的時間
        
start = time.ticks_ms()-60*1000#應用程式啟動時，計時時間，先減60秒
    
time1=Timer()
time1.init(mode=Timer.PERIODIC, freq=1,callback=callback1)