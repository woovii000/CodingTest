def solution(phone_book):
    # phone_book의 원소 중에 번호 겹침o -> False
    # 겹침x -> True
    for i in range(len(phone_book)-1):
        for j in range(1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return False
    return True