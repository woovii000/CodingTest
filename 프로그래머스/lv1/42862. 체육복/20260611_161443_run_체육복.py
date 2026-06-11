def solution(n, lost, reserve):
    # lost.value == reserve.value => 제외(pop)
    # lost.value+-1 == reserve.value => 제외(pop)
    # n - len(lost)
    lost.sort()
    reserve.sort()
    for x in lost:
        if x in reserve:   
            lost.remove(x)
            reserve.remove(x)
    answer = 0
    return answer