def solution(name):
    # 상하
    change = 0
    for c in name: # 자리마다
        diff = ord(c)-ord('A') # A 사이 간격
        change += min(diff, 26-diff) # 둘 중 최소
        
    # 좌우
    n = len(name)
    move = n-1 # 오른쪽 한 방향 시, 최소
    for i in range(n):
        next_idx = i+1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        move = min(move, i*2 + n-next_idx) # 우 찍고, 좌 꺾기
        move = min(move, (n-next_idx)*2 + i) # 좌 찍고, 우 꺾기
    
    return change + move