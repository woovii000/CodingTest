def solution(numbers):
    # 방법1. 만들 수 있는 경우의 수 찾고 필터링*
    count = 0 # 소수 개수
    split = list(numbers) # 문자열 list화
    n = len(split) # 문자들의 개수
    used = [False] * n # **
    all_num = set() # 조합 숫자
    
    def dfs(path):
        num = int(path)
        if num not in all_num:
            all_num.add(num)
        
        if len(all_num) == n:
            return
        
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            dfs(path + split[i])
            used[i] = False
        
    dfs("")
    n = len(all_num)
    for i in range(2, 0.5*n+1):
        if n%i == 0:
            break
        else:
            count += 1
    
    return count
            
    