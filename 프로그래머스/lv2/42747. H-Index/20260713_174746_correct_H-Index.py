def solution(citations):
    answer = 0 # H-Index 없을 경우 대비 초기화
    # i: 1~n편
    for i in range(1, len(citations)+1):
            count = 0 # 편수마다 초기화
            # j: idx - 0~n-1
            for j in range(len(citations)):
                    # i번이상 인용된 논문 수 구하기 + i번이하 인용된 논문 필터링
                    if i < citations[j]:
                            count += 1
            # i번이상 인용된 논문 수 조건 확인
            if count >= i:
                    answer = i
    # 모든 구간을 돌고 최종 최댓값 확인
    return answer