def solution(s):
    # s의 0 을 제거 -> '1111...'
    # 그때 len(s) -> n
    # len(s) -> 2진 변환
    
    # s -> 1 될 때 까지 '2진 변환'
    # 그때까지의 2진변환 횟수(count), 과정에서 제거된 0 갯수(zero) => [count, zero] 로 반환
    
    # s: str -> list화 -> 0 제거 + zero++ -> len()''.join(list)) -> 숫자를 2진 변환 -> 1Cycle => while 문 반복 (s != 1)까지

    # 간소화) s의 0갯수 세기(zero++), 1갯수 = n -> 2진화 -> s'으로 사이클 무한 반복
    answer = []
    count, zero = 0, 0
    while ''.join(list(s)) != '1':
        
    return [count, zero]