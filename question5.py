# 5 0 

# 2 -2 0 3 4 

# Sample Output 1 

# 1 

N=int(input("Size of Array: ")) # how many elements
Array=[]
Array_check=[]
for i in range(N):
    Array_nos=int(input("enter elements in array: "))
    Array.append(Array_nos)
Number_Check=int(input("Enter no you want to check in Array: "))

if Number_Check in Array:
    print(1)
else:
    print(0)

