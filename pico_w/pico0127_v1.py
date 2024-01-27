from machine import Pin, Timer, PWM, ADC

def fun10(t:Timer | None = None):
    print('10秒了!!!')
    led_red.toggle()

led_red = Pin(15, mode=Pin.OUT)
timer10 = Timer(period=1000, mode=Timer.PERIODIC, callback=fun10)

while True:
    pass


#led_red = Pin(15, mode=Pin.OUT)
#led_red.value(0)
#led_red.value(1)