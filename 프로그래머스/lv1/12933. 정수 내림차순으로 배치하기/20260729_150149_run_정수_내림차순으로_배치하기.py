def solution(n):
    x = list(map(int,str(n)))
    sorted(x, reversed)
    return int(''.join(x))