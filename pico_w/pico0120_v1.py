from machine import Pin
import time
led_red = Pin(15, mode=Pin.OUT)
button_red = Pin(14, mode=Pin.PULL_DOWN)
is_press = False

while True:
    #time.sleep_ms(500) = 0.5秒 (1000)=1秒
    #time.sleep_ms(500)
    #數值1代表True
    if button_red.value():
        is_press = True
        led_red.value(1)
    elif is_press:
        print('釋放')
        is_press = False
        led_red.value(0)


#led_red.off() > 關燈
#led_red.on() > 開燈
#led_red.value(0) > 關燈
#led_red.value(1) > 開燈
#led_red.low() > 關燈
#led_red.high() > 開燈
