def solution(n, lost, reserve):
    # lost.value == reserve.value => 제외(pop)
    # lost.value+-1 == reserve.value => 제외(pop)
    # n - len(lost)
    lost.sort()
    reserve.sort()
    lost_c, reserve_c = lost[:], reserve[:]
    # 도난 + 여벌 유저
    for x in lost:
        if x in reserve:   
            lost_c.remove(x)
            reserve_c.remove(x)
    # 여벌옷 빌려주기
    return n - len(lost_c)