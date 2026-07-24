def solution(k, dungeons):
    answer = 0
    visited = [False]*len(dungeons)
    def gone(heal, count):
        nonlocal answer
        answer = max(answer, count)
        for i in range(len(dungeons)):
            need, lose = dungeons[i]
            
            if not visited[i] and heal >= need:
                visited[i] = True
                gone(heal-lose, count+1)
                visited[i]=False
    gone(k,0)
    return answer