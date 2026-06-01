def solution(my_string, queries):
    arr = list(my_string) # 효율적
    for s, e in queries:
        for i in range(0,(e-s+1)//2):
            arr[s+i], arr[e-i] = arr[e-i], arr[s+i]
    return "".join(arr)