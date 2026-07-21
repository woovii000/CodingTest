def solution(numbers):
    # 방법1. 만들 수 있는 경우의 수 찾고 필터링*
    split = list(numbers) # 숫자 나누기
    n = len(split) # 나눠진 수 문자
    used = [False]*n # 조합 생성위한 사용 여부
    all_case = set() # 조합숫자 셋(중복 제외)

    # 조합 만들기
    def dfs(path):
            # 문자열 있고, 조합 셋에 없는지 확인
            if path and int(path) not in all_case:
                all_case.add(int(path))
            for i in range(n):
                    used[i] = True
                    dfd(path+split[i])
                    used[i] = False
    dfs("")
    count = 0 # 소수 개수
    # 조합 요소의 소수 판별
    for num in all_case:
        is_prime = False
        # n에 대한 곱셈 조합 - 2~sqrt(n)까지만 찾기
        for i in range(2, num**0.5+1):
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
            
    