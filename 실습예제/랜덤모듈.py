# 랜덤 모듈 불러오기
# 하단 터미널에 import random

#1~10까지의 숫자중 랜덤으로 하나가 출력
#random.randint(1,10) 
import random
import myModule as my

x = random.randint(0, 1)

if x == 1:
    print("앞면")
else:
    print("뒷면")

print(my.pi)