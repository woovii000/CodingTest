def solution(name):
    # 자리 -> [0]부터 각 자리 A부터 시작. len(alpha): 26
    # 각자리 알파벳 이동 min(x, 26-x)
    change = 0
    for c in name:
        diff = org(c)-org('A')
        change += min(diff, 26-diff) # 알파벳 별 최소 이동
    
    n = len(name)
    move = n-1 # 0기준, 한 방향
    for i in range(n):
        next_idx = i+1
        
        # 연속되는 A의 끝 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        # 오른쪽 갔다가 꺾기
        move = min(move, 2*i + n-next_idx)
        
        # 왼쪽 갔다가 꺾기
        move = min(move, 2*(n-next_idx) + i)

    return change+move