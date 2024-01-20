from machine import Pin
import time
led_red = Pin(15, mode=Pin.OUT)
button_red = Pin(14, mode=Pin.PULL_DOWN)
is_press = False
#稱之為switch的按鈕
led_red_status = False

def toggle_led():
    global led_red_status
    global is_press
    if button_red.value():
        time.sleep_ms(50)
        is_press = True
        #led_red.value(1)
    elif is_press:
        #第一次收到0的訊號，0.05秒後再紀錄
        time.sleep_ms(50)
        if not button_red.value():
        #not後面要加布林值
            led_red_status = not led_red_status
            led_red.value(led_red_status)
            is_press = False
            if led_red_status:
                print("請停止")
            else:
                print("請通過")

while True:
    toggle_led()
    
#led_red.off() > 關燈
#led_red.on() > 開燈
#led_red.value(0) > 關燈
#led_red.value(1) > 開燈
#led_red.low() > 關燈
#led_red.high() > 開燈
    
#time.sleep_ms(500) = 0.5秒 (1000)=1秒
#time.sleep_ms(500)
#數值1代表True
