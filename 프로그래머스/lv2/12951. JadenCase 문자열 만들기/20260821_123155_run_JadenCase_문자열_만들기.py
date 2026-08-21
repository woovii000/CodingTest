def solution(s):
    # 글자(str -> 불변) 나누기
    words = s.split(" ")
    
    for idx in range(len(words)):
        # 불변 -> list로 가변화
        ch = list(words[idx])
        for i in range(len(ch)):
            # 맨 앞글자[0] 소문자, 대문자 => 대문자 변환
            if i == 0 and ch[i].isalpha():
                ch[i] = ch[i].upper()
            # 이후 뒷글자[1~n] 대문자,소문자 -> 소문자
            elif ch[i].isalpha():
                ch[i] = ch[i].lower()
            # 나눈 문자 붙이기
            words[idx] = ''.join(ch)
    return ' '.join(words)