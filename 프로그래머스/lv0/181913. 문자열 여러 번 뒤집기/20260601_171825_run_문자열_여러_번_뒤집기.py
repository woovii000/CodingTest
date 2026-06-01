def solution(my_string, queries):
    arr = []
    for ch in my_string:
        arr += ch
    for s, r in queries:
        for i in range((s+r/2)):
            arr[s+i], arr[r-i] = arr[r-i], arr[s+i]
    return "".join(arr)