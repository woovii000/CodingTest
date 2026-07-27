def solution(word):                                      
    answer = 0
    vowel = ['A','E','I','O','U']
    w = []
    def dfs(make):
        nonlocal answer
        count = 0
        for i in vowel:
            if make and ''.join(make) == word:
                answer = count
                break
            if len(make)==5:
                break
            make.append(i)
            count += 1
            dfs(make)
            make.pop() # 백트래킹
    dfs(w)
    return answer