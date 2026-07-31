def solution(phone_number):
    # 뒷자리 4개 제외 *
    n = list(phone_number)
    for i in range(len(n)):
        if i < len(n)-4: 
            n[i] = '*'
    return ''.join(n)