import urequests as requests
from machine import Pin, Timer, ADC
from tools import connect, reconnect
import time

def fun10(t:Timer | None = None):
    light_value=light.read_u16()
    vr_value=vr.read_u16()
    url=f'https://blynk.cloud/external/api/batch/update?token=OjsaRz73dEbe7wlmUomfBRB38u8kSMj6&v0={light_value}&v1={vr_value}'
    try:
        led_red.value(1)
        response = requests.get(url)
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("server有錯誤訊息")
        response.close()
    led_red.value(0)

def fun500ms(t:Timer):
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')
    
connect()
light = ADC(Pin(28))
led_red = Pin(15, mode=Pin.OUT)
vr = ADC(Pin(27))
timer10 = Timer(period=500, mode=Timer.PERIODIC, callback=fun10)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)



#led_red = Pin(15, mode=Pin.OUT)
#led_red.value(0)
#led_red.value(1)
