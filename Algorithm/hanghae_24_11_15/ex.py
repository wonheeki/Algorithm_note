A = input()
B = input()
# 2. 문자열을 공백 기준으로 쪼갬
arr_A = A.split()

# print(arr_A)
answer = 0

# 3. for문으로 arr_A을 하나하나 비교
for item in arr_A:
    # 3=1 문제의 조건에 맞춰 필터링
    if item != B and item[0] == B[0] and item[1] == B[1]:
        # 통과되면 answer 1up
        answer += 1

print(answer)