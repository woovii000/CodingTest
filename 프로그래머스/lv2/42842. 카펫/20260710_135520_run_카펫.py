def solution(brown, yellow):
    # n*m 형태 -> 조합 찾기?
    carpet = brown+yellow
    for i in range(carpet):
        for j in range(i+1,carpet):
            if i*j == carpet:
                return [i,j]