def factorial(n):
    # 런타임 에러 발생 n==0 인 조건 추가
    # if n == 1:
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)


n = int(input())
print(factorial(n))

