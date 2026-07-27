def solution(word):
    answer = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    w = list()
    fin = False
    def dfs(start):
        for v in vowel:
            if fin:
                return
            if ''.join(start) == word
                fin = True
                
            start.append(v)
            answer += 1 
            
            if len(start) < 5:
                dfs(start)
        
    dfs(w)
    return answer