import sys

## 문제 상황
## isPalindrome 결과값을 반환하고,
## recursion 함수가 호출된 횟수를 반환함
def recursion(s, l, r,cnt):
    # global cnt
    cnt+=1
    if l >= r: return 1,cnt
    elif s[l] != s[r]: return 0,cnt
    else: return recursion(s, l+1, r-1,cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)


n = int(input())
list =[]
for _ in range(n):
    # list.append(sys.stdin.readline().rstrip())
    list.append(isPalindrome(sys.stdin.readline().rstrip()))


for item in list:
    cnt, ispalin = item
    print(cnt, ispalin)