def solution(number, k):
    # 가장 큰수를 만들려면, 가장 작은 수를 빼면되지않나?
    # 맨 앞에서 가장 작은 수를 먼저 빼는 방식* x
    # -> 스택() + 다음 숫자가 나보다 큰가?
    num = []
    
    for n in number:
        while num and k > 0 and num[-1] < n:
            num.pop()
            k -= 1
        num.append(n)
        
    if k > 0:
        num = num[:len(num)-k]
    return ''.join(num)