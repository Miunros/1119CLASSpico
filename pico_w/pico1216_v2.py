from machine import Timer
def mycallback(t):
    print(1)
def mycallback2(t):
    print(2)
time1 = Timer()
time1.init(mode=Timer.PERIODIC,freq=1,callback=mycallback)#每1秒輸出1

time2 = Timer()
time2.init(mode=Timer.PERIODIC,period=3000,callback=mycallback2) #每3秒輸出2