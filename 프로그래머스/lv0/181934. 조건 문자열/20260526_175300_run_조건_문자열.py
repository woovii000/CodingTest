def solution(ineq, eq, n, m):
    if ineq == '>' and eq == "=":
        return int(n>=m)
    elif ineq == '<' and eq == "=":
        return int(n<=m)
    elif ineq == '>' and eq == "!":
        return int(n>m)
    elif ineq == '<' and eq == "1":
        return int(n<m)