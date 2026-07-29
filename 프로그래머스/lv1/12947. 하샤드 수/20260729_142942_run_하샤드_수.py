def solution(x):
    hasha = 0
    string = str(x)
    for c in string:
        hasha += int(c)
    return (True if hasha%x==0 else False)