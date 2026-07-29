def solution(x):
    hashad, string = 0, str(x)
    for c in string:
        hashad += int(c)
    return (True if x%hashad==0 else False)