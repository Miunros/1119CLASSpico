import random
import pyinputplus as pyip
while(True):
    min = 1
    max = 100
    count = 0
    randomNum = random.randint(min, max)
    print(randomNum)
    print("***********終極密碼***********")
    while True:
        keyin = pyip.inputInt(f"請猜數字，範圍是{min}~{max}:", min=min, max=max)
        print(keyin)
        count +=1
        if (keyin == randomNum):
            print(f"恭喜你賓果!!!!答案是：{randomNum}")
            print(f"您猜了:{count}次")
            break
        elif (keyin < randomNum):
            print("再大一點!!!")
            min = keyin +1
        elif (keyin > randomNum):
            print("再小一點!!!")
            max = keyin -1 
        print(f"您已經猜了{count}次")
    is_play = pyip.inputYesNo("您還要繼續玩嗎?(輸入Yes, No)")
    if is_play=="no":
        break
print("遊戲結束!!!")
