def solution(answers):
    # 정답 패턴
    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    # 정답 수
    check = [0,0,0]
    answer = []
    # 정답 체크 -> 정답? +1
    for i in range(len(answers)):
        if pattern[0][i%5] == answers[i]:
            check[0] += 1
        if pattern[1][i%8] == answers[i]:
            check[1] += 1
        if pattern[2][i%10] == answers[i]:
            check[2] += 1   
    # 최고점 확인
    for i in range(len(check)):
        if check[i] == max(check):
            answer.append(i+1)
    return answer