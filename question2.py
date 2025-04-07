# Q2. You are given an array of strings, whose size is stored in a variable with the name N. 
# The string array, is stored in a variable with the name arr. 
# You have to find how many of the strings stored in the array arr, are weak, and how many of them are strong. 
# A string is considered as strong if it contains at least one of the following characters in it @,$,#,* 
# Consider the example, in which the value stored in N = 4, and the array,arr = ["test123", "new@t", "mon*y", "nrupul"] 
# The first string "test123", does not contain any of the required characters, hence the string is weak 
# The second string "new@t", contains the character `@`, hence the string is strong 
# The third string "mon*y", contains the character `*`, hence the string is strong 
# The fourth string "nrupul", does not contain any of the required characters, hence the string is weak 




# for i in Array_of_Strings:
#     if i is

string="test123"
for i in string:
    if i is '@'or i is"#":
        print('strong')
    else:
        print("weak")



Array_of_Strings = ["test123", "new@t", "mon*y", "nrupul"]
Single_String = ["@", "$", "#", "*"]

for i in Array_of_Strings:
    for j in Single_String:
        if j in i:
            print('strong')
            break
    else:
        print("weak")
