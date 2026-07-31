def solution(phone_number):
    # 뒷자리 4개 제외 *
    0-10->11-4
    phone_number[:len(phone_number)-4] = *
    return phone_number