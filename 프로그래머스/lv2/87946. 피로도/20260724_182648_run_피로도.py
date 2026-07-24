def solution(k, dungeons):
    count = 0
    gone = [False]*len(dungeons)
    def can_go(heal):
        if heal: # 0인지 확인
            return
        for i in range(len(gone)):
            if not gone[i]:
                gone[i] = True
                if count > dungeons[i][0]:
                    count += 1
                    can_go(count - dungeons[i][1])
                gone[i] = False
    can_go(k)
    return count