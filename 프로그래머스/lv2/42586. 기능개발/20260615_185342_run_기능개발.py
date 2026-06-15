def solution(progresses, speeds):
    answer = []
    n = 0
    a = 0
    while a != len(progresses):
        for i in range(len(progresses[:])):
            progresses[i] += speeds[i]
        for i in range(a,len(progresses[:])):
            if progresses[i] >= 100:
                n += 1
                a += 1
        answer.append(n)
        n=0
    return answer