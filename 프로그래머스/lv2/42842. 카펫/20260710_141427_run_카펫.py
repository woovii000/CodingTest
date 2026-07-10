def solution(brown, yellow):
    # g*s 형태(g >= s) -> 조합 찾기
    # 2중 for문
    carpet = brown + yellow
    if carpet//2 == 0:
        for se in range(carpet//2):
            for ga in range(se+1,carpet//2):
                if ga*se == carpet and ga-se <= 2 and ga-se >= 0:
                    return [ga,se]
    else:
        i = 1
        while i:
            if i*i == carpet:
                return [i,i]
            i += 1