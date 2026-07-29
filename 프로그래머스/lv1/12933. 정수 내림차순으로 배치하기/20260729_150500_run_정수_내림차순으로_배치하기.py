def solution(n):
    x = list(str(n))
    x.sort(reverse=True)
    return int(''.join(x))