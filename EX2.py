# 06. 문자열을 입력 받아서 역순으로 리턴
def backward_string(val):
    return ?

if __name__ == '__main__':
    print(backward_string('val'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'


# 07. 리스트 items 와 정수 i를 입력받아,
#만약 i가 items에 있으면 i 앞의 숫자들을 제거하고 리턴
def remove_all_before(items, i) 
    # 코드 작성
    return ? 

if __name__ == '__main__':
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    
    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]


# 08. text 문자열을 입력받아 문자열의 문자가 모두 대문자 이면 True 리턴,
# 소문자가 있으면 False 리턴, 빈' ' 문자열이나 중간의 ' ' 는 True 로 한다.
def is_all_upper(text):
    return ?
    
if __name__ == '__main__':
    print(is_all_upper('ALL UPPER'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True


# 09. 리스트를 입력받아 첫번째 아이템을 맨 마지막으로 보낸다음 리턴, 빈 리스트 [ ] 나 [ 1 ] 하나의 값이 있을때는 같은 리스트가 리턴

def replace_first(items):
    #코드작성      
    return ?
   
if __name__ == '__main__':
    print(list(replace_first([1, 2, 3, 4])))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []


# 10. 양수를 입력받아서 숫자의 자릿수중에 가장 큰수(0~9)가 리턴
def max_digit(number):
    return ?

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    ```