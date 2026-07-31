def solution(phone_number):
    # 뒷자리 4개 제외 *
    for n in phone_number:
        n = map(*,n)
    return phone_number