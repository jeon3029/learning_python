x = [1,2,3,4]
y = x
x[2] = 100
print(y) # 1,2,100,4
print(x) # 1,2,100,4

y = list(x)
x[2] = 0
print(x) # 1,2,0,5
print(y) # 1,2,100,4