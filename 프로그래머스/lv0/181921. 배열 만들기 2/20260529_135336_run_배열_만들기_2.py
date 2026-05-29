def solution(l, r):
    answer = []
    for i in range(1,r+1):
        if set(str(i)) == {'0','5'}:
            answer.append(i)
    return answer