import time
from machine import Pin
led = Pin("LED", Pin.OUT)
while True:
    led.value(1)
    time.sleep(1)  #表示在這裡停1秒不要動
    led.value(0)
    time.sleep(1)	#繼續執行