# 파이썬의 기본 데이터 타입
# int - 정수형 데이터
# float - 소수점을 포함한 실수
# bool - 참 거짓
# None - Null과 같은 표현

a = 7
b = 7.777
c = True
d = False
e = "문자열"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(2/4)
# 같은 2/4인데 위에는 소수점표시 아래는 float로 표시가된다 자동형변환
print(type(2/4))

# 제곱과 나누기
print(2**3)  # 2*2*2 = 8
print(5//2)  # 나누기의 몫이 2
print(5 % 2)  # 1

# 반올림 round(숫자 , 자릿수) 숫자를 자릿수 만큼 반올림을 한다
print(round(3.156, 2))
# 위의값이 소수점 두자리에서 반올림했기때무에 값이 3.16이 출력됨
