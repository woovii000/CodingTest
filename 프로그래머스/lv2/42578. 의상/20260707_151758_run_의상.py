def solution(clothes):
    # clothes[i][1] 을 키로 해서 값이 있으면 +1 없으면 key value 추가
    # {k1: a, k2: b, ...}
    categories = {}
    for i in range(len(clothes)):
        if clothes[i][1] in categories:
            categories[clothes[i][1]] += 1
        else:
            categories[clothes[i][1]] = 1
    # 경우의 수 계산**
    answer = 1
    for ch in categories:
        answer *= categories[ch]+1
    # 키 1개
    if len(categories) == 1:
        return answer
    # 안 입는 경우(1개) 뺴기
    else: 
        return answer-1