def solution(a, d, included):
    # a+(n-1)d
    sum = 0
    for i in range(len(included)):
        if included[i]:
            sum += a+i*d
        else:
            sum
    return sum