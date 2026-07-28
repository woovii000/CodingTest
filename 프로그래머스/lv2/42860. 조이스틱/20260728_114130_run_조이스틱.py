def solution(name):
    # 자리 -> [0]부터 각 자리 A부터 시작. len(alpha): 26
    # 각자리 알파벳 이동 min(x, 26-x)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = 0
    left, right = 0, 0
    d = list() # 이동할 위치 list
    
    for c in name:
        if c != 'A':
            d.append(name.index(c)) # 이동할 위치 idx
        x = alpha.index(c)
        answer += min(x, 26-x) # 알파벳 별 최소 이동
    
    n = len(name)
    drive = list()
    
    # 이동할 위치
    for i in range(len(d)-1): # idx 0 -> not A
        drive.append((d[i],d[i+1])) # (di, si)
        
    # 자리 별 최소 이동
    for di, si in drive:
        right += di-si
        left += abs(-n+di-si)
        
    answer += min(left, right)
    return answer