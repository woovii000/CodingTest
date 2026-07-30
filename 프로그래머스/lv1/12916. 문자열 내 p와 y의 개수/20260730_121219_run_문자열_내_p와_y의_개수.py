def solution(s):
    count = 0
    for ch in s:
        if ch == 'P' or ch == 'p':
            count += 1
        if ch == 'Y' or ch = 'y':
            count -= 1
    if not count:
        return True
    return False