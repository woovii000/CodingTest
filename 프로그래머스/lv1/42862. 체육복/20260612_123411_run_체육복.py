def solution(n, lost, reserve):
    # lost.value == reserve.value => 제외(pop)
    # lost.value+-1 == reserve.value => 제외(pop)
    # n - len(lost)
    lost.sort()
    reserve.sort()
    lost_c, reserve_c = lost[:], reserve[:]
    for x in lost:
        if x in reserve:   
            lost_c.remove(x)
            reserve_c.remove(x)
    for x in lost:
        if x+1 in reserve:
            lost_c.remove(x)
            reserve_c.remove(x+1)
    return n - len(lost_c)