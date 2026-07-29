def solution(n):
    x = list(map(int, str(n)))
    x.sort(reverse=True)
    return x