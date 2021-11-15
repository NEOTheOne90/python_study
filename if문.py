# if 문 문법
if True : 
    print("조건이 참이면 실행")
    print("실행코드는 띄어쓰기로 구분")
    #if 문의 코드블록은 띄어쓰기로 된곳까지 
elif a == b:
    print("a b가 같다")
else : #if문의 조건이 거짓이면 코드 실행 
    print("if문의 조건이 거짓일때 실행") 
print("종료")

# 예제 1) 숫자를 입력받아서 홀수/짝수를 출력하라
#  🚨 여기 코드는 수정 안합니다.👇
number = int(input("숫자를 입력: \n"))
# 🚨 여기 코드는 수정 안합니다. 👆

#아래에 코드 작성👇
if (number % 2 == 0) :
    print("짝수 입니다.")
else : 
    print("홀수 입니다.")

#예제 2)놀이공원의 청룡열차는 키가 120cm보다 커야 탈수있고
#나이에따라서 요금을 따로 받습니다.
#12살 미만 5000원, 12 18살사이 7000원 19살 이상 12000원
#  🚨 여기 코드는 수정 안합니다.👇
height = int(input("키를 cm로 입력해 주세요: \n"))
# 🚨 여기 코드는 수정 안합니다. 👆

#아래에 코드 작성👇
if  height > 120:
    print("청룡열차를 탈수 있습니다.")
    age = int(input("나이를 입력해 주세요: \n"))

    if age < 12: #12살 미만
        print("요금은 5000원 입니다.")
    elif age <= 18: #12살 이상 18살 이하
        print("요금은 7000원 입니다.")
    else: #19살 이상
        print("요금은 12000원 입니다.")
else:
    print("죄송하지만 탈 수 없습니다.")
