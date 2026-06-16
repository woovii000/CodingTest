def solution(progresses, speeds):
    answer = []
    p = len(progresses)
    while sum(answer) != p:
        n = 0
        for i in range(p):
            progresses[i] += speeds[i]
        for i in range(sum(answer),p):
            if progresses[i] < 100:
                break
            elif progresses[i] >= 100:
                n += 1
        if n !=0 :
            answer.append(n)
    return answer