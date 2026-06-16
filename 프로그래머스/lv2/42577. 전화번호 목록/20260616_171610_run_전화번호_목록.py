def solution(phone_book):
    # phone_book의 원소 중에 번호 겹침o -> False
    # 겹침x -> True
    # 포인트: 접두어* -> startswith()
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            elif phone_book[j].startswith(phone_book[i]):
                return False
    return True