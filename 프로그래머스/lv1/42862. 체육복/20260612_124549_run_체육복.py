def solution(n, lost, reserve):
    # lost.value == reserve.value => 제외(pop)
    # lost.value+-1 == reserve.value => 제외(pop)
    # n - len(lost)
    lost.sort()
    reserve.sort()
    lost_c, reserve_c = lost[:], reserve[:]
    answer = []
    # 도난 + 여벌 유저
    for x in lost:
        if x in reserve:   
            lost_c.remove(x)
            reserve_c.remove(x)
            answer.append(x)
    # 여벌옷 빌려주기
    for x in lost_c:
        if x-1 in reserve_c:
            reserve_c.remove(x-1)
            answer.append[x]
        elif x+1 in reserve_c:
            reserve_c.remove(x+1)
            answer.append[x]
    return answer