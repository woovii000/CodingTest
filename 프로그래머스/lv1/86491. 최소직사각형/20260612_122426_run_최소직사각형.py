def solution(sizes):
    # 가로 세로 비교 정렬
    # 정렬한 길이들로 가장 큰거 정하기
    for a, b in sizes:
        a = min(a,b)
        b = max(a,b)
    ga = []
    se = []
    for i in range(len(sizes)):
        ga.append(size[i][0])
        se.append(size[i][1])
    return max(ga)*max(se)