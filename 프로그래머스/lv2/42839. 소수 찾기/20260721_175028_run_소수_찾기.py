def solution(numbers):
    # 방법 - 만들 수 있는 경우의 수 찾고 필터링*
    split = list(numbers) # 숫자 종이 나누기(list화)
    n = len(split) # 나눠진 문자 개수
    used = [False]*n # 조합 생성위한 사용 여부
    all_case = set() # 빈 조합숫자 셋(중복 제외)

    # 조합 만들기
    def dfs(path):
        # 문자열 있고, 조합 셋에 없는지 확인
        if path and int(path) not in all_case:
            all_case.add(int(path)) # int화 + 추가
        # path의 길이 최대일 때, 끝
        if len(path) == n:
            return
        # 조합 케이스 이어서 하기(완전탐색)**
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            dfs(path + split[i])
            used[i] = False
    
    dfs("") # 조합 숫자 채우기
    count = 0 # 소수 개수
    
    # 조합 요소의 소수 판별
    for num in all_case:
        is_prime = False # 소수 판별(T/F)
        # n에 대한 곱셈 조합 - 2~sqrt(n)까지만 찾기
        for i in range(2, int(num**0.5)+1):
            if n%i == 0:
                break
            else:
                is_prime = True
                break
        # n == 소수 -> count++
        if is_prime:
            count += 1
            is_prime = False

    return count
            
    