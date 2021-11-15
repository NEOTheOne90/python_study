# 예제 점심값 내기
# 학생들 이름을 받아서 분리 
# 랜덤함수를 이용해 학생들의 숫자에 맞는 랜덤정수 생성
# 당첨자를 선택한다. 리스트의 인덱스 번호 이용
import random
# 🚨 여기는 그대로 👇
names_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적습니다.\n")
names = names_string.split(",")
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇
print(names)
#print(len(names))

n = random.randint(0,len(names)) 
# 랜덤 인덱스 숫자(사람수 만큼)
print (f" 오늘 커피는{names[n]}가 쏩니다!")