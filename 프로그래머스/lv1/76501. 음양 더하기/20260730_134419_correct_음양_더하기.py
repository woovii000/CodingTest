def solution(absolutes, signs):
    nums = [x if s else -x for x, s in zip(absolutes, signs)]
    return sum(nums) 