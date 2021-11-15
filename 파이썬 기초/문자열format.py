# 1. f - string
name = '홍길동'
age = 20
print(f'안녕하세요{name}님 나이가 {age}살 이군요')

# 2. 문자열.format()
number = 20
welcome = '환영합니다'

print('{}번 손님 {}'.format(number, welcome))

# 예제 1 변수 name과 color에 자신의 이름과 좋아하는 색상을 문자열로 입력
name = '장한별'
color = '노랑색'
print(f'안녕하세요 제 이름은 {name}이고 좋아하는색상은 {color} 입니다.')
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))


# 문자열 인덱스 : 문자열은 인덱스 번호를 사용가능

string1 = "abcdefg"
print(string1[2])  # c
print(string1[1:5])  # bcde 1번부터 5번까지 짜르기
print(string1[1:])  # 1번없이 끝까지

# 슬라이싱 [시작 : 끝], [: : 증감]
print(string1[::-1])  # 뒤에서 처음까지

# 인덱스 번호로 값을 가져오는것은 가능하지만 수정불가
string1[0] = 'k'
