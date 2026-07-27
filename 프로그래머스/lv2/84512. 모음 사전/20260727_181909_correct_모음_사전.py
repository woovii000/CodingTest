def solution(word):
    answer = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    w = list()
    fin = False
    def dfs(start):
        nonlocal answer, fin
        for v in vowel:
            if fin:
                return
            
            start.append(v)
            answer += 1
            
            if ''.join(start) == word:
                fin = True
                return
            
            if len(start) < 5:
                dfs(start)
            
            start.pop()
    dfs(w)
    return answer