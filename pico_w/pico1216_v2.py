from machine import Pin,Timer

def mycallback(t:Timer):
    print(1)

def mycallback2(t:Timer):
    print(2)

led = Pin("LED", Pin.OUT)

while True:
    led.high()  # 打開 LED
    time1 = Timer()  # 創建 Timer 物件
    time1.init(mode=machine.Timer.PERIODIC, freq=1,callback=mycallback)  # 每1秒觸發 mycallback
    led.low()  # 關閉 LED
    time2 = Timer()  # 創建另一個 Timer 物件
    time2.init( mode=machine.Timer.PERIODIC, freq=3,callback=mycallback2)  # 每3秒觸發 mycallback2
