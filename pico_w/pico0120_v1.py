from machine import Pin
import time
led_red = Pin(15, mode=Pin.OUT)
button_red = Pin(14, mode=Pin.PULL_DOWN)

while True:
    #time.sleep_ms(500) = 0.5秒 (1000)=1秒
    print(button_red.value())
    time.sleep_ms(500)
    
#led_red.off() > 關燈
#led_red.on() > 開燈
#led_red.value(0) > 關燈
#led_red.value(1) > 開燈
#led_red.low() > 關燈
#led_red.high() > 開燈
