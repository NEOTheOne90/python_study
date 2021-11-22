#11/22연습문제
# 01.두 수의 곱을 리턴하는 함수

def mult_two(a, b):
    #함수를 완성시킨다.
    return a*b

if __name__ == '__main__':
  print(mult_two(3,2))
 #다음과 같이 리턴결과가 나와야 한다.
  assert mult_two(3,2) == 6
  assert mult_two(1,0) == 0


# 02.듀플(3개 입력 이상) 을 입력받아서
# 첫번째 값, 세번째 값, 끝에서 두번째 값을 듀플로 만들어 리턴
def easy_unpack(e):
    return (e[0], e[2], e[-2])  # 튜플로 리턴 (1, 3, 7 의 각위치의 숫자불러옴 )

if __name__ == '__main__':
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)


# 03. 한 단어만 끊어서 리턴한다.
#만약 끊어진 단어가 없다면 단어 전체 리턴
def first_word(text):
  return text.split()[0] # split사용으로 첫번째 공백을 읽어준다.

if __name__ == '__main__':
    print(first_word("Hello world"))
    
    # 다음과 같이 리턴결과가 나와야 한다.
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"


# 04. 패스워드는 길이가 6보다 커야 한다. => 크면 True 틀리면 False 리턴
def is_acceptable_password(password):
    return len(password) > 6 # len사용해서 문자열 길이를 받는다.
    
if __name__ == '__main__':
    print(is_acceptable_password('short'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False


# 05. 정수(int)의 길이를 구하라.
def number_length(a):
    return len(str(a))

if __name__ == '__main__':
    print(number_length(10))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
