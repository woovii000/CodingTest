def solution(brown, yellow):
    # n*m 형태 -> 조합 찾기?
    # 2중 for문
    carpet = brown+yellow
    for i in range(carpet//2):
        for j in range(i+1,carpet//2):
            if i*j == carpet and j-i <= 2:
                return [i,j]