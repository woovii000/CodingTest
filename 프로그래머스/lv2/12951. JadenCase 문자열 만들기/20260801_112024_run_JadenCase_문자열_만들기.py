def solution(s):
    words = list(s.split(' '))
    for i in range(len(words)):
        if words[i][0] >= '0' and words[i][0] <= '9':
            words[i][0].upper()
    return ' '.join(words)