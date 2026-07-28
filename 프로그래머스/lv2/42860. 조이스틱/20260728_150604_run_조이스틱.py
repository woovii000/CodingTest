def solution(name):
    change = 0
    # 상하
    for c in name:
        diff = ord(c)-ord('A') # 바꿀 때, 클릭
        change = min(diff, 26-diff) # 둘 중 최소
        
    # 좌우
    n = len(name)
    move = n-1 # 오른쪽 한 방향 시, 최소
#     for i in range(n):
#         next_idx = i+1
#         while next_idx < n and name[i] == 'A':
#             next_idx += 1
        
#         move = min(move, i*2 + n-next_idx) # 오른쪽 찍고, 왼쪽 꺾기
#         move = min(move, (n-next_idx)*2 + i)# 오른쪽 찍고, 왼쪽 꺾기
    
    return change + move