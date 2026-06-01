def solution(number):
    num = int(number)
    sum = 0
    while num>10:
        sum += num%10
        num = num//10 
    return sum%9