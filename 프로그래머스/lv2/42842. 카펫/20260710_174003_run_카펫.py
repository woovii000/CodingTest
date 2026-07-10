def solution(brown, yellow):
    # g*s 형태(g >= s) -> 조합 찾기
    # 카펫 패턴 - i**2 , n*m
    # b, y
    carpet = brown + yellow
    for se in range(carpet//2):
        for ga in range(carpet//2):
            if ga*se == carpet and ga-se >=0 and (ga-1)*(se-1)==yellow:
                return [ga,se]