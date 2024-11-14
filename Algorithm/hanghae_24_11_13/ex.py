N = int(input())
# 1부터 N까지 별의 개수 증가해라
for i in range(0, N + 1):
    # 별 출력 end="" : 줄바꿈 방지
    print("*" * i, end=" ")
    # 공백 출력
    print(" " * (2 * (N - i)), end="")
    # 별 출력
    print("*" * i)

# N-1부터 1까지 별의 개수 감소
for i in range(N-1, 0, -1):
    # 별 출력
    print("*" * i, end="")
    # 공백 출력
    print(" " * (2 * (N - i)), end="")
    # 별 출력
    print("*" * i)