def solution(k, dungeons):
    answer = 0
    visited = [False]*len(dungeons) # 방문 여부
    def dfs(fatigue, count):
        nonlocal answer # 전역변수
        answer = max(answer, count) # 현재 방문 수 최댓값 확인
        
        for i in range(len(dungeons)): # 첫 방문여부로 돌기
            need, use = dungeons[i] # 최소, 소모 피로도
            # 방문x, k>최소 피로도 -> 방문 가능
            if not visited[i] and k >= need:
                visited[i] = True # 방문처리 + 다음 방문 진행
                dfs(k-use, count+1)
                visited[i] = False
    
    dfs(k,0)
    return answer