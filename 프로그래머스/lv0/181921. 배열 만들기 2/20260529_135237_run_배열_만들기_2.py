def solution(l, r):
    answer = []
    for i in range(1,r+1):
        if '5' in str(i) and '0' in str(i):
            answer.append(i)
    return answer