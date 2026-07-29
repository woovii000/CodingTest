def solution(n):
    x = list(str(n))
    return int(''.join(x.sort(reverse=True)))