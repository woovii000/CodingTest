def solution(phone_number):
    # 뒷자리 4개 제외 *
    phone = list(phone_number)
    for i in range(0,len(phone)-4):
        phone[i] = *
    return ''.join(phone)