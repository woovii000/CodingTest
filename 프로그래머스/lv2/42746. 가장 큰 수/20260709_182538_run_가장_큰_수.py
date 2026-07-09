def solution(numbers):
    # 흐름 numbers 속 숫자 -> 문자 변환+케이스별로 이어붙이기-> 숫자 변환 ->str(max(케이스)) 반환
    # 위에는 말 그대로 했을 떄, 낭비
    
    # 핵심 - 맨 앞 자리가 크면 됨 -> a+b b+a 일 때 앞자리 비교
    
    # [] -> 문자열 변환
    for i in range(len((numbers))): 
        numbers[i] = str(numbers[i])
        
    # 힌트 - .sort(key=lambda x: x*3, reverse=True)**
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    # 이어붙이기
    answer = ''
    for ch in numbers:
        answer += ch
        
    # 정수 변환 시, 0인 경우
    if int(answer) == 0:
        return '0'
    return answer