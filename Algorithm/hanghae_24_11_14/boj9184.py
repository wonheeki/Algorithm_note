import sys
#
# def w(a,b,c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif(a > 20 or b > 20 or c > 20):
#         return w(20, 20, 20)
#     elif(a < b and b < c):
#         return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#     else :
#         return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)


dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

arr =[]
while True:
    a,b,c =map(int,sys.stdin.readline().split())
    if a==-1 and b ==-1 and c ==-1:
        break
    arr.append([a,b,c])
print(arr)

for item in arr :

    print('w({},{},{}) = {}'.format(item[0],item[1],item[2],w(item[0],item[1],item[2])))
    # print("w(", end="")
    # print(*item,sep="," ,end="")
    # print(") = ",end="")
    # print(w(item[0],item[1],item[2]))

