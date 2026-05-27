def solution(code):
    mode = 0
    answer = []
    for idx, ch in enumerate(code):
        if ch == 1:
            mode = 0 if mode == 1 else 1
        else:
            if mode == 0:
                if idx%2==0:
                    answer += ch
            else:
                if idx%2==1:
                    answer += ch
    return "".join(answer)