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
    # 키가 1개 -> 키값 
    if len(categories) == 1:
        return # 키값 - 키 어떻게 구할건데?
    # 키 n개 -> 종류+1(안 입는 경우) 곱하고 -1(다 안 입는 경우)
    else:
        answer = 1
        for ch in categories:
            answer *= categories[ch]+1
        return answer-1