def solution(n):
    if isinstance(n**0.5,int):
        return 1
    for i in range(1, (n**0.5)+1):
        if i**2 == n:
            return (i+1)**2