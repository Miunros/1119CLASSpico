from machine import ADC, Timer
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
    #溫度如果超過23度每5秒會發一次通知
    if temp >=23 and delta>=5*1000:
        alert()
        start = time.ticks_ms()
        
start = time.ticks_ms()-60*1000
    
time1=Timer()
time1.init(mode=Timer.PERIODIC, freq=1,callback=callback1)