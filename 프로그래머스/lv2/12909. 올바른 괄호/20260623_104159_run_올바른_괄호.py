def solution(s):
    # ( 만나면 스택 )만나면 지우면서 (팝
    # ) 시작 -> false
    answer = []
    for i in range(len(s)):
        if s[i] == "(":
            answer.append(s[i])
        elif s[i] == ")" and not answer.empty():
            answer.pop()
    return !answer