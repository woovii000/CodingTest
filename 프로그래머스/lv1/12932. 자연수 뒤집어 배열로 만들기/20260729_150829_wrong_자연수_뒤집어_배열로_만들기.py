def solution(n):
    n = list(map(int, str(n)))
    n.sort(reverse=True)
    return n