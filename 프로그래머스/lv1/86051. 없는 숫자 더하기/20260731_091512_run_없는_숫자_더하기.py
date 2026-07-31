def solution(numbers):
    # list 만들고 빼버리기
    n = [0,1,2,3,4,5,6,7,8,9]
    x = [x if x not in n for x in numbers]
    return sum(n)