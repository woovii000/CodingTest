def solution(code):
    mode = 0
    answer = []
    for idx in range(len(code)):
        if code[idx] == 1:
            mode = 0 if mode == 1 else 1
        else:
            if mode == 0:
                answer = answer+code[idx] if idx%2==0
            else:
                answer = answer+code[idx] if idx%2==1
    return answer