def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        sec = 0
        for j in range(i+1,len(prices)):
            if j == len(prices)-1:
                sec = 0
            elif prices[i] > prices[j]:  
                sec = 1
                break
            else:
                sec += 1
        answer.append(sec)
    return answer

# 실패. o(n**2) -> x