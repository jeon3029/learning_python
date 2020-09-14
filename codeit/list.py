# list
numbers=[2,3,5,7,11,13]
names=["A","B","C","D"]

#indexing
print(names[0])
print(numbers[-2])

#slicing
print(numbers[0:3])
print(names[2:])
print(names[:2])
print(numbers[-2:])
new = numbers[:3]
print(new[2])

numbers[0] = 7
print(numbers)

#len, append
print(len(numbers))
numbers.append(5)
numbers.append(8)
print(len(numbers))

#insert delete
del numbers[3]
print(numbers)
names.remove("A")
print(names)

numbers.insert(4,3)
print(numbers)

#sort sorted
new = sorted(numbers)
print(new)
new = sorted(numbers,reverse=True)
print(new)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)

numbers.reverse()
print(numbers)

#in
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)
print(12 not in primes)

#index

print(primes.index(11))