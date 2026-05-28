def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        #queries[i][0]<= i <=queries[i][1]
        if queries[i][2] < min(arr[queries[i][0]:queries[i][1]+1]):
            answer.append(min(arr[queries[i][0]:queries[i][1]+1]))
    if answer :
        return "".join(answer)
    return -1;