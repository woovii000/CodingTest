def solution(a, b):
    s = 0
    for m, n in zip(a,b):
        s += m*n
    return s