def solution(name):
    # 자리 -> [0]부터 각 자리 A부터 시작. len(alpha): 26
    # 각자리 알파벳 이동 min(x, 26-x)
    n = len(name)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    change = 0
    
    for c in name:
        x = alpha.index(c)
        change += min(x, 26-x) # 알파벳 별 최소 이동
    
    move = n-1 # 0기준, 한 방향
    for i in range(n):
        nxt_idx = i+1
        
        # 연속되는 A의 끝 찾기
        while nxt_idx < n and name[nxt_idx] == 'A':
            nxt_idx += 1
        
        # 오른쪽 갔다가 꺾기
        move = min(move, 2*i + n-nxt_idx)
        
        # 왼쪽 갔다가 꺾기
        move = min(move, 2*(n-nxt_idx) + i)

    return change+move