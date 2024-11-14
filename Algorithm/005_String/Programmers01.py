def solutions(s):
    answer = len(s)

    # 1개 단위(step) 부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ''

        # 앞에서 부터 step 까지의 문자열 추출
        prev = s[0:step]
        count = 1

        # 단위 (step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 홧수 (count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면 (더이상 압축을 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # 다시 상태 초기화
                prev = s[j:j + step]
                count = 1

        #남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer