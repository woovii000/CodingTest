def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        min_value = float('inf')
        for i in range(s, e+1):
            if k < arr[i]:
                min_value = min(min_value, arr[i])
        answer.append(min_value if min_value != float('inf') else -1)
    return answer