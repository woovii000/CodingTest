def solution(a, d, included):
    # a+(n-1)b
    sum = 0
    for i in range(len(included)):
        if included[i]:
            sum += a+i*b
        else:
            sum
    return sum