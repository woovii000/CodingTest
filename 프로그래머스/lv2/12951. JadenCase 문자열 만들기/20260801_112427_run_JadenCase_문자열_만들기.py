def solution(s):
    words = list(s.split(' ')) # 단어 나누기
    for word in words: # 단어 별 작업
        for i in range(len(word)): # 단어의 문자별 작업
            if word[i] >= '0' and word[i] <= '9':
                continue
            elif i == 0:
                word[i].upper()
            else:
                word[i].lower()
    return ' '.join(words)