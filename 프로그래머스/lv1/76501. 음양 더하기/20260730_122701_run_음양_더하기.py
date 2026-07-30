def solution(absolutes, signs):
    nums = [x for x, s in zip(absolutes, signs) if s else -x ]
    return sum(nums) 