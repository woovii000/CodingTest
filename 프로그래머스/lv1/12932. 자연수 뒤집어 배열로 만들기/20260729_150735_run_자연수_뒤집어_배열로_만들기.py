def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    n = map(int, n)
    return n