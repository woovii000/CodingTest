def solution(n):
    x = list(map(int,str(n)))
    return int(''.join(x.sort(reverse=True)))