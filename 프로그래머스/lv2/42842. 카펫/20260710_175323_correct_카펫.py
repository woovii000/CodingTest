def solution(brown, yellow):
    # g*s 형태(g >= s) -> 조합 찾기
    # 카펫 패턴 - i**2 , n*m
    # b, y
    carpet = brown + yellow
    for se in range(2,carpet):
        for ga in range(2,carpet):
            if ga*se == carpet and ga-se >=0 and (ga-2)*(se-2)==yellow:
                return [ga,se]