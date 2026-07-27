def solution(word):                                      
    answer = 0
    vowel = ['A','E','I','O','U']
    w = []
    def dfs(make):
        nonlocal answer
        for i in vowel:
            if make and ''.join(make) == word:
                break
            make.append(i)
            answer += 1
            dfs(make)
    dfs(w)
    return answer