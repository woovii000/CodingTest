def solution(phone_number):
    # 뒷자리 4개 제외 *
    n = list(phone_number)
    for i in range(len(n)):
        n[i] = * if i > len(n)-4 else n[i]
    return ''.join(n)