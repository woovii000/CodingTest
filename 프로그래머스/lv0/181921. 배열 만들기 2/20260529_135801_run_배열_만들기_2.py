def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if set(str(i)) != {'1','2','3','4','6','7','8','9'}:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer