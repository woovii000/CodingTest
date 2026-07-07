def solution(clothes):
    # clothes[i][1] 을 키로 해서 값이 있으면 +1 없으면 key value 추가
    # {k1: a, k2: b, ...}
    categories = {}
    for i in clothes:
        if clothes[i][0] in categories:
            categories[clothes[i][0]] += 1
        else:
            categories[clothes[i][0]] = 1
    # 경우의 수 계산**
    
    # 만약 키가 1개 -> 키값 
    return 0