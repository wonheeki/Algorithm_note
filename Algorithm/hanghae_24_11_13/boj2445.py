n = int(input())

# for i in range(0,n*2-1):
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(n*2-2):
#         print(" ",end="")
#     for j in range(i + 1):
#         print("*",end="")
#     print()


for i in range(1,n+1):
    print("*"*i+" "*((n*2)-(i*2))+"*"*i)
for j in range(n-1,0,-1):
    print("*" *j + " " * ((n * 2) - (j * 2)) + "*" * j)


