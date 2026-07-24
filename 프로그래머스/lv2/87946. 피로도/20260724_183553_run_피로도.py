def solution(k, dungeons):
    count = 0
    gone = [False]*len(dungeons)
    def can_go(heal, count):
        nonlocal count
        for i in range(len(gone)):
            if not gone[i]:
                gone[i] = True
                if heal >= dungeons[i][0]:
                    can_go(heal - dungeons[i][1],count+1)
                    gone[i] = False
    can_go(k,count)
    return count