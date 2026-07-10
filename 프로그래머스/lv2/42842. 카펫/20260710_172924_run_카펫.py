def solution(brown, yellow):
    # g*s 형태(g >= s) -> 조합 찾기
    # 2중 for문
    carpet = brown + yellow
    for se in range(carpet//2):
        for ga in range(carpet//2):
            if ga*se == carpet and ga-se <= 10 and ga-se >= 0:
                return [ga,se]