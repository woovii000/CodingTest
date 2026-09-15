def solution(clothes):
    categories = {} # dict
    
    for i in range(len(clothes)):
        if clothes[i][1] in categories:
            categories[clothes[i][1]] += 1
        else:
            categories[clothes[i][1]] = 1
        
    answer = 1
    for ct in categories:
        answer *= categories[ct]+1
    return answer-1