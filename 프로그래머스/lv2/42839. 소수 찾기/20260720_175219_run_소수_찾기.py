def solution(numbers):
    # 방법1. 만들 수 있는 경우의 수 찾고 필터링*
    # 방법2. 처음부터 찾아버리기(기각)
    count = 0
    ch = list(numbers) # 문자열 -> 배열
    
    n = len(digits)
    used = [False] * n
    num = set()

    def dfs(path):
        # 1자리 이상이면 숫자로 변환해서 집합에 넣기
        if path:
            num = int(path)
            if num not in result_set:  # 미리 중복 확인 후 삽입
                result_set.add(num)

        if len(path) == n:
            return  # 더 이상 붙일 문자 없음

        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            dfs(path + digits[i])
            used[i] = False

    dfs("")

    # set 순회 -> 소수 판별** -> count++
    for n in num:
        for i in range(2, n*0.5 +1):
            if n%i==0:
                break
            else:
                count += 1
    return count