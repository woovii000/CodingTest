def solution(arr, queries):
    # answer = []
    for s,e,k in queries:
        for i in range(s,e+1):
            arr[i] = arr[i]+1 if arr[i]%k==0 else arr[i]
    return arr