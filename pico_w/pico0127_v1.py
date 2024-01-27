from machine import Pin, Timer, PWM, ADC
import time

def fun10(t:Timer | None = None):
    print('10秒了!!!')
    led_red.toggle()

def fun10ms(t:Timer | None = None):
    print(light.read_u16())
light = ADC(Pin(28))
led_red = Pin(15, mode=Pin.OUT)

timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer10ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)



#led_red = Pin(15, mode=Pin.OUT)
#led_red.value(0)
#led_red.value(1)