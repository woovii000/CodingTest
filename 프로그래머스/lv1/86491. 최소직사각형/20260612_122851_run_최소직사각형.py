def solution(sizes):
    # 가로 세로 비교 정렬
    # 정렬한 길이들로 가장 큰거 정하기
    for i in range(len(sizes)):
        low, high = min(sizes[i][0],sizes[i][1]), max(sizes[i][0],sizes[i][1])
        sizes[i][0], sizes[i][1] = low, high 
    ga = []
    se = []
    for i in range(len(sizes)):
        ga.append(sizes[i][0])
        se.append(sizes[i][1])
    return max(ga)*max(se)