def solution(number, k):
    answer = '' # 만들 숫자

    # 숫자 넣기
    for i in number:
        while answer and k>0 and int(answer[-1])>=int(i):
            answer.pop()
            k -= 1
        answer.add(i)
        
    
    # 아직 뺄 숫자o
    if k > 0:
        answer = answer[:-k]
        
    return ''.join(answer)