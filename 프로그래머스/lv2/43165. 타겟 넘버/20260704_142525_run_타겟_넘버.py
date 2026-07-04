def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer #?
        
        # 종료 조건
        if index == len(numbers):
            if total == target:
                return # answer = 가능방법 수
        # 현재 숫자를 더하는 경우
        
        
        # 현재 숫자를 빼는 경우
    
    dfs(index, total)
    
    return answer