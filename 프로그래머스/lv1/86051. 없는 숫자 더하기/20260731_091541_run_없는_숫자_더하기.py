def solution(numbers):
    # list 만들고 빼버리기
    n = [0,1,2,3,4,5,6,7,8,9]
    x = [x for x in numbers if x not in n]
    return sum(x)