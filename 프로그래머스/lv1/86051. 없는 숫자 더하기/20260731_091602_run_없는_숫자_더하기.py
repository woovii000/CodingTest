def solution(numbers):
    # list 만들고 빼버리기
    n = [0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        if num not in n:
            n.pop(n.index(num))
    return sum(n)