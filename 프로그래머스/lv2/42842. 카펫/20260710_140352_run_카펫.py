def solution(brown, yellow):
    # n*m 형태 -> 조합 찾기?
    # 2중 for문
    carpet = brown+yellow
    for ga in range(carpet//2):
        for se in range(i+1,carpet//2):
            if ga*se == carpet and ga-se <= 2 and ga-se >= 0:
                return [i,j]