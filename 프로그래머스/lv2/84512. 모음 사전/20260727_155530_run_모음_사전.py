def solution(word):                                      
    answer = 0
    vowel = ['A','E','I','O','U']
    w = []
    def dfs(make):
        nonlocal answer
        for i in vowel:
            if make and ''.join(make) == word:
                return
            if len(make)==5:
                return
            make.append(i)
            answer += 1
            dfs(make)
            make.pop()
    dfs(w)
    return answer