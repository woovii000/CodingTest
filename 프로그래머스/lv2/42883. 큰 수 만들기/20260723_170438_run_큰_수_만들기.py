def solution(number, k):
    # 가장 큰수를 만들려면, 가장 작은 수를 빼면되지않나?
    # 맨 앞에서 가장 작은 수를 먼저 빼는 방식* x
    # -> 스택() + 다음 숫자가 나보다 큰가?
    num = [] # 스택
    for n in number: # 순회
        while num[-1] < n:
            num.pop() # 넣은 숫자들 빼기
        num.append(n) # number에서 선별해 넣기
    
    if len(num) > len(number)-k :
        num = num.pop()
    return ''.join(num)