def solution(name):
    # 자리 -> [0]부터 각 자리 A부터 시작. len(alpha): 26
    # 각자리 알파벳 이동 min(x, 26-x)
    n = len(name)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = 0
    left, right = 0, 0
    d = list() # 이동할 위치 list
    
    for i in range(len(name)):
        if name[i] != 'A':
            d.append(i) # 이동할 위치 idx 확보
        x = alpha.index(name[i])
        answer += min(x, 26-x) # 알파벳 별 최소 이동
    if name[0] == 'A':
        d.insert(0,0)
    # 이동 방향 별 최소 이동
    for i in range(len(d)-1):
        right += d[i+1]-d[i]
        left += abs(-n+d[i+1]-d[i])
        
    answer += min(left, right)
    return answer