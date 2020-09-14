# 사전(dictionary)
# key-value pair
my_dic = {
    5:25,
    2:4,
    3:9
}
print(my_dic)
print(my_dic[3])
my_dic[9] = 81
print(my_dic[9])


for val in my_dic.values():
    print(val)
for key in my_dic.keys():
    print(key)
for key,value in my_dic.items():
    print(key,value)

