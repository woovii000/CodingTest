def solution(a, b):
    if a > b:
        return sum([x for x in range(b,a+1)])    
    return sum([x for x in range(a,b+1)])