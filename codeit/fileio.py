with open('./data/chicken.txt','r') as f:
    print(type(f))
    for line in f:
        print(line,end="")
    for line2 in f:
        print(line2.strip())

# 'a' 는 append
with open('./data/new_File.txt','w') as f:
    f.write("Hello World\n")
    f.write("My name is TJ")