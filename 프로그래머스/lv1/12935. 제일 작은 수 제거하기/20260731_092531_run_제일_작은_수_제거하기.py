def solution(arr):
    if arr.remove(arr.min()) is None:
        return [-1]
    return arr.remove(arr.min())