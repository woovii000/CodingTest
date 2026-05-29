def solution(arr, queries):
    answer = arr
    for s,e,k in queries:
        for i in range(s,e+1):
            answer[i] = answer[i]+1 if arr[i] !=0 and arr[i]%k==0 else answer[i]
    return arr