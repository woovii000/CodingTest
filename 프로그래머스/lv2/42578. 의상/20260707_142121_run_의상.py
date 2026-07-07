def solution(clothes):
    # clothes[i][1] 을 키로 해서 값이 있으면 +1 없으면 key value 추가
    # {k1: a, k2: b, ...}
    categories = {}
    for i in range(len(clothes)):
        if clothes[i][0] in categories:
            categories[clothes[i][0]] += 1
        else:
            categories[clothes[i][0]] = 1
    # 경우의 수 계산**
    # 키가 1개 -> 키값 
    if len(categories) == 1:
        return len(categories)
    # 키 n개 - sum(키값) + 키1값*키2값 + 모든 경우의 수;;
    else:
        
        return 0