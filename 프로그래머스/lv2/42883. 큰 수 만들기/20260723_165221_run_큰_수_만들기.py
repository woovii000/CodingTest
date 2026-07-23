def solution(number, k):
    # 가장 큰수를 만들려면, 가장 작은 수를 빼면되지않나?
    # 맨 앞에서 가장 작은 수를 먼저 빼는 방식* x
    # -> 스택() + 다음 숫자가 나보다 큰가?
    count = 0
    num = []
    for n in number: # 일단 넣기
        if not num:
            num.append(n)
            continue
        elif count < k and num[-1] <= n:
            num.pop(-1)
            num.append(n)
            count += 1
            continue
        elif num[-1] > n: 
            num.append(n)
            continue
            
    while count < k:
        num.pop(-1)
        count += 1
            
    return num