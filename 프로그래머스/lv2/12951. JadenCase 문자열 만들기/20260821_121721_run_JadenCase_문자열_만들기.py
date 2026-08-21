def solution(s):
    # 글자 나누기 + 붙이기
    words = s.split(" ")
    for ch in words:
        if ch = "":
            continue
        for i in range(len(ch)):
            # 맨 앞글자[0] 소문자, 대문자 => 대문자 변환
            if i == 0 and ('a' < ch[i] or 'z' > ch[i]):
                ch[i] = ch[i].upper()
            # 이후 뒷글자[1~n] 대문자,소문자 -> 소문자
            elif 'A' < ch[i] or 'Z' > ch[i]:
                ch[i] = ch[i].lower()
    
    # 나눈 문자는 " "를 사이 문자로 해서 붙이고 출력
    return ' '.join(words)