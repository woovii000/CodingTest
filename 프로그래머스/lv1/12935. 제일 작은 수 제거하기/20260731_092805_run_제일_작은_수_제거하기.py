def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        return arr.remove(min(arr))