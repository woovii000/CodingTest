def solution(k, dungeons):
    answer = 0 
    visited = [False]*len(dungeons)
    
    def gone(figure, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            need, lose = dungeons[i] # 언박싱
            if not visited[i] and figure>=need:
                visited[i] = True
                gone(figure - need, count+1)
                visited[i] = False
            
    gone(k,0)
    return answer