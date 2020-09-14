#split

my_str = "1. 2. 3. 4. 5. 6."
print(my_str.split(". "))

full_name = "Kim, Yuna"
print(full_name.split(", "))
name_data = full_name.split(", ")
first_name = name_data[0]
last_name = name_data[1]
print(first_name,last_name)

#white space 로 split
print("  \n\n 2  \t 3 \n 7 7 11 \n\n".split())