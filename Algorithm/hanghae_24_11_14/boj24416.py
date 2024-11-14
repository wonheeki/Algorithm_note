n = int(input())

def fib(n):
    cnt1 = 0
    if n==1 or n==2:
        cnt1 += 1
        return 1  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n) :
    cnt2=0
    # 배열 f를 크기 n+1로 초기화 (0으로 채워진 리스트)
    f = [0] * (n + 1)
    f[1] = f[2] = 1  # f[1]과 f[2]를 1로 초기화

    # 3부터 n까지 반복하며 피보나치 수열을 계산
    for i in range(3, n + 1):
        cnt2+=1
        f[i] = f[i - 1] + f[i - 2]  # 이전 두 항의 합

    return cnt2  # n번째 피보나치 수 반환



print(fib(n),fibonacci(n))