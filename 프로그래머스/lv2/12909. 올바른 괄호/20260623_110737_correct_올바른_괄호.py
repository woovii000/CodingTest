def solution(s):
    # ( 만나면 스택 )만나면 지우면서 (팝
    # ) 시작 -> false
    answer = 0
    for i in range(len(s)):
        if s[0] == ")":
            return False
        elif s[i] == "(":
            answer += 1
        elif s[i] == ")" and answer:
            answer -= 1
    return not answer