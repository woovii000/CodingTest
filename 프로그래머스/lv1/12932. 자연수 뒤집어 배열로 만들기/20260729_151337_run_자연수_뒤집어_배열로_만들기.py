def solution(n):
    num = list()
    while n > 0:
        num.append(n%10)
        n = n//10
    return num