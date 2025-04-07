# 50 40 30 20 10
N=int(input("Size of Array: ")) # how many elements
Array=[]
Array_check=[]
for i in range(N):
    Array_nos=int(input("enter elements in array: "))
    Array.append(Array_nos)

print("Youar array is",Array)
Operation=int(input("Enter how many operations you want to perform: "))

for i in range(Operation):
    Operation_no=int(input("Enter no you want to check in Array: "))
    Array_check.append(Operation_no)
    for  j in Array_check:
        if j in Array:
            print('Yes')
        else:
            print('No')
