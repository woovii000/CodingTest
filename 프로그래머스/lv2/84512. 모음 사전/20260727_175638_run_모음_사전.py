def solution(word):
    answer = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    w = list()
    fin = False
    def dfs(start):
        nonlocal answer, fin
        if not fin: # 단어 못 찾음 -> 진행
            for v in vowel:
                
                if ''.join(start) == word: # 단어 찾음 -> 끝
                    fin = True
                    start.pop() # ?
                
                if len(start) > 5:
                    start.pop()
                
                start.append(v)
                answer += 1
                dfs(start)
                start.pop()
    dfs(w)
    return answer