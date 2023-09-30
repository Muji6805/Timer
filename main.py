import time
import os
pm = 1

def timer(t):
    if t < 60:
        print(str(t) + "초")
        time.sleep(1)
    else:
        m = int(t / 60)
        t %= 60
        print(str(m) + "분", str(t) + "초")
        time.sleep(1)

while True:
    if pm < 300:
        os.system("cls")
        timer(pm)
        pm += 1
    else:
        os.system("cls")
        print("5분이 지났습니다\n다음 문제로 넘어가십시오")
        break