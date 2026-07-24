def solution(k, dungeons):
    answer = 0 
    visited = [False]*len(dungeons)
    
    def gone(figure, count):
        nonlocal answer
        answer = max(answer, count) # 다녀온 횟수
        
        for i in range(len(dungeons)): # 던전 순회
            need, lose = dungeons[i] # 언박싱
            # no 방문 & 최소 피로도 있는가
            if not visited[i] and figure>=need:
                visited[i] = True
                gone(figure - need, count+1)
                visited[i] = False
            
    gone(k,0)
    return answer