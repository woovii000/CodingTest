def solution(phone_number):
    # 뒷자리 4개 제외 *
    n = list(phone_number)
    n[i] = '*' if i < len(n)-4 else n[i] for i in range(len(n)) 
    return ''.join(n)