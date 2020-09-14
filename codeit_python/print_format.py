year = 2020
month = 10
day = 29
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year,month,day))
print(date_string.format(year,month,day+1))

print("저는 {0}, {1}, {0}, {2}를 좋아합니다".format("박지성","유재석","빌게이츠"))

num1 = 2
num2 = 3
# 소수점 셋째자리에서 반올림
print("{0} 나누기 {1} 는 {2:.2f} 입니다".format(num1,num2,num1/num2))

# 다른 방법
name = "홍길동"
age = 33
print("제 이름은 %s이고 %d살입니다." % (name, age)) # 고전적인 방법
print(f"제 이름은 {name}이고 {age}살입니다.") # python 3.6부터 사용할 수 있는 방법