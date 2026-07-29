def solution(n):
    answer = -1
    for i in range(n):
        if n == i**2:
            return (i+1)**2 
    return answer