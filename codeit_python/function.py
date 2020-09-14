def hello():
    print("Hello")
    print("welcome to codeit")


def square(a):
    return a*a


print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

# function with return

def square2(x):
    print("함수 시작")
    return x*x
    print("함수 끝") # doesn't execute

def myself(name, age, nationality="한국"):# 옵셔널 파라미터는 마지막에
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우