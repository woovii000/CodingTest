def solution(s):
    # ' '기준 자르고 -> 숫자화 => list String
    minmax = list(map(int, s.split()))
    # min() max() -> return f'{min} {max}'
    mi = min(minmax)
    ma = max(minmax)
    return f"{mi} {ma}"