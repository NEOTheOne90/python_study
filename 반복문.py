# while 반복문

#while True:
#    print("무한반복")
# CTRL + C 하면 멈춤

#count = 0
#while count < 3:
#    print('횟수: ', count)
#    count += 1

#name = ''
#while name != '펭수': #name이 펭수가 되면 종료
#  name = input('펭수를 입력해 주세요 : ')

#print("thank you")

#hit = 0
#while hit < 10:
#    hit += 1
#    print(f'나무를 {hit}번 찍었습니다.')
#    if hit == 10:
#        print("나무 넘어갑니다.")

for n in [1,2,3]:
    print(n)

for s in ['다람쥐' , '펭귄' , '돌고래', '강아지']:
    print(s)

for c in '홍길동님':  #문자열의 철자를 한글자씩 반복한다.
    print(c)

# for반복문과 자주쓰는 함수 range(시작, 끝) 리턴값은 시작~ 끝-1
for n in range(3):
    print(n)
# 1에서 100까지의 합은
total = 0
for x in range(1,101):
    total += x

print("1에서 100까지 더한값: ", total)

# 구구단 2단
for i in range(1, 10):
    print(f'2 X {i} = {2*i}')

# 예제 구구단 2단부터 9단까지 
# 전체 구구단 출력 반복문을 중첩 이중반복문
# 매개변수 end를 사용해서 가로로 한줄식 출력한다.
for i in range(2,10):
    print()
    for j in range(1,10):
        print(f'{i} X {j} ={i*j}', end=" ")