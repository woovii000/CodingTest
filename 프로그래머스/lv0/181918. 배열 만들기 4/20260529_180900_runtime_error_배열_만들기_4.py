def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk:
            while stk[-1]>=arr[i]: #***
                stk.pop()
            stk.append(arr[i])
        else:
            stk.append(arr[i])
    return stk