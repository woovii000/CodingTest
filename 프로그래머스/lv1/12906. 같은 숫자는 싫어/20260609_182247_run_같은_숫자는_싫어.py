def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # range vs enumerate()
    for n in arr:
        if not answer:
            answer.append(n)
        elif answer[-1] == n:
            continue
        else:
            answer.append(n)
    return answer