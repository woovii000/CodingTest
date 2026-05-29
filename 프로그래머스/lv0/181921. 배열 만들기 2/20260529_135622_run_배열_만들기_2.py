def solution(l, r):
    answer = []
    for i in range(l-1,r+1):
        if set(str(i)) == {'0','5'}:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer