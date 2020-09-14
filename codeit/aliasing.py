x = [1,2,3,4]
y = x
x[2] = 100
print(y)
print(x)

y = list(x)
x[2] = 0
print(x)
print(y)