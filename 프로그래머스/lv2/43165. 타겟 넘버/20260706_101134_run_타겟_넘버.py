def solution(numbers, target):
    answer = 0
    
    # 깊이 탐색
    def dfs(index, result):
        nonlocal answer = 0 # 동명 변수 - 지역변수화 차단
        if index == len(numbers): # 모든 idx 갔을 때,
            if result == target: # 결과 == 해답 숫자
                answer += 1 # 방법 +1
                return
        dfs(index+1, result+numbers[index]) # 다음 idx 숫자 더할 때
        dfs(index-1, result-numbers[index]) # 다음 idx 숫자 뺄 때
        
    dfs(0,0) # 탐색 시작
    
    return answer