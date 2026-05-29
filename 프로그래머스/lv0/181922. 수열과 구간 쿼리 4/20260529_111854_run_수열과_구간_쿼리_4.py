def solution(arr, queries):
    answer = arr[:]
    for s,e,k in queries:
        for i in range(s,e+1):
            answer[i] = answer[i]+1 if i%k==0 else answer[i]
    return answer