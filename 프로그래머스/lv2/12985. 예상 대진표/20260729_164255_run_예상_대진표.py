def solution(n,a,b):
    index = 0
    # n == 2**i -> 1~i회내로 a,b 만남
    for i in (1,20):
        if 2**i == n:
            index = i
    def dfs(i):
        if i<=1:
            return 
        if (a <= 2**(i-1) and b > 2**(i-1)) or (b <= 2**(i-1) and a > 2**(i-1)):
            return i
        else:
            dfs(i-1)
    dfs(index)