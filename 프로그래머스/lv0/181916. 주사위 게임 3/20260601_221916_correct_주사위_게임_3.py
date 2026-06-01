# set(), count()
def solution(a, b, c, d):
    arr = [a,b,c,d]
    # 모두 같을 때
    if len(set(arr)) == 1:
        return 1111*arr[0]
    elif len(set(arr)) == 2:
        p, q = 0, 0
        for i in set(arr):
            # 세 개가 같을 때
            if arr.count(i) == 3:
                p = i
            elif arr.count(i) == 1:
                q = i
        if p!=0:
            return (10*p+q)**2
                
        # 2개*2세트가 같을 때
        else:
            nums = list(set(arr))
            return (nums[0]+nums[1])*abs(nums[0]-nums[1])
    # 2같 1,1 다름
    elif len(set(arr)) == 3:
        others = []
        for i in set(arr):
            if arr.count(i) !=2:
                others.append(i)
        return others[0] * others[1]
    # 모두 다를 때
    else:
        return min(arr)