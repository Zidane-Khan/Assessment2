# Q3. You are given a number, stored in a variable with the name N 
# Print N lines such that on each line, all the numbers in the range of [1,N] are printed in reverse order 
# For example, consider the value stored in N = 5 
# Therefore, the output required will be 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# N=5
# N2=[]
# for i in range(N-1):
#     N2.append(i)
# print(N2)

# # for i in range(N-1,-1,-1):
# #     print(N[i],end="")


N=int(input("range you want: "))
for j in range(N):
    for i in range(N,-1,-1):
        if i==0:
            continue
        print(i,end=" ")
    print("\n")
        
