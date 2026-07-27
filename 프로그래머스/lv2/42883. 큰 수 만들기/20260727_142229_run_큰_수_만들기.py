def solution(number, k):
    answer = list() # 만들 숫자
    n = len(number)

    for c in number:
        while k>0:
            if int(answer[-1]) < int(c):
                answer.pop()
                k -= 1
        answer.append(c)
    
    if k > 0:
        num = num[:-k]
        
    return ''.join(num)