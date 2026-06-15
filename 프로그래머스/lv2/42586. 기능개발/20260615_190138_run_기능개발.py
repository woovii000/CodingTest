def solution(progresses, speeds):
    answer = []
    p = len(progresses)
    a = sum(answer)
    while a != p:
        n = 0
        for i in range(p):
            progresses[i] += speeds[i]
        for i in range(a,p):
            if progresses[i] < 100:
                continue
            elif progresses[i] >= 100:
                n += 1
        if n !=0 :
            answer.append(n)
    return answer