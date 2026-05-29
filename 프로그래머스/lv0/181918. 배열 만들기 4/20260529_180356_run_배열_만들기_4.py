def solution(arr):
    stk = []
    while i<=len(arr):
        if stk:
            if stk[-1]<arr[i]:
                stk.push(arr[i])
            else:
                stk.pop(stk[-1])
        else:
            stk.push(arr[i])
        i += 1
    return stk