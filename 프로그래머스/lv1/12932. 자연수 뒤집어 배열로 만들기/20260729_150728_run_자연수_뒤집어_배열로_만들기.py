def solution(n):
    n = list(str(n))
    n.sort(revers=True)
    n = map(int, n)
    return n