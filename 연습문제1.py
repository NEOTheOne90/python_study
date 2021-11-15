# 예제1) 다음코드의 실행 결과는?
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")  #wife 가 없어서 거짓
elif "python" in a and "you" not in a:
    print("python") #pyton은 있고 you없어야 참인데 있어서 거짓
elif "shirt" not in a:
    print("shirt")  #shirt없어야 참 , 없어서 참
elif "need" in a:
    print("need") 
else:
    print("none")

# 예제2) while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.
i = 1
result = 0 
while i <= 1000 :
    if (i % 3 == 0) :
        result += i
    i += 1
print(result)

# 예제3) while문을 사용하여 다음과 같이 *을 표시하는 프로그램작성
# *
# **
# ***
# ****
# *****
n = 5
i = 1
while i <= n:        #조건문 코드를 완성하자
    print('*' *i ) #문자열 * 숫자만큼 반복
    i += 1