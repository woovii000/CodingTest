def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        sec = []
        for j in range(queries[i][0],queries[i][1]+1):
            if queries[i][2] < arr[j]:
                sec.append(arr[j])
        if sec:
            answer.append(min(sec))
        else:
            answer.append(-1)
    return answer