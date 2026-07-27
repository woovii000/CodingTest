def solution(number, k):
    answer = list() # 만들 숫자

    # 숫자 넣기
    for i in number:
        # 만들 숫자 안 빔, 뺄 숫자o, 앞 숫자보다 뒤가 클 때
        while answer and k>0 and int(answer[-1])<int(i):
            answer.pop() # 빼
            k -= 1 # 뺀 숫자 차감
        answer.append(i)
        
    
    # 아직 뺄 숫자o
    if k > 0:
        answer = answer[:-k] # 뒤에서 k개만큼 뺌
        
    return ''.join(answer)