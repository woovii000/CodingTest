def solution(name):
    # len: 26
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 자리 -> [0]부터 각 자리 A부터 시작.
    # 각자리 알파벳 이동 min(x, 26-x)
    answer = 0
    n = len(name)
    for c in name:
        x = alpha.index(c)
        answer += min(x, 26-x) # 알파벳
        #
        # if c != 'A'
        #     answer += min(x,n-x) # 자리 이동
    return answer