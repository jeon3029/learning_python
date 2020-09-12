def add(a,b):
    return a+b
def swap(a,b):
    return b,a
a = int(input("정수 1 입력 : "))
b = int(input("정수 2 입력 : "))
sum = add(a,b)
average = sum/2
print("합 : ",sum)
print("평균 :",average)
a,b = swap(a,b)
print("두수의 교환 : %d %d" %(a,b))
