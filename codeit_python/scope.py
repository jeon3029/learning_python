y = 2 # 글로벌 변수
def my_function():
    x=3
    y=3# local y / global y 해줘야 됨
    print(x)

my_function()
#print(x) # x doesn't exist
print(y) #2


