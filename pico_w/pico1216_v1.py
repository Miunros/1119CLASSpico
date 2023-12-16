import time
from machine import Pin
led = Pin("LED", Pin.OUT)
while True:
    led.high()
    time.sleep_ms(500)  #表示在這裡停1秒不要動
    led.low()
    time.sleep(1)	#繼續執行