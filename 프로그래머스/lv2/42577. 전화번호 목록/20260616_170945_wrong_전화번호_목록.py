def solution(phone_book):
    # phone_book[0] -> phone_book[1], phone_book[2] 중에 겹치면 False 아님 True
    for i in range(1, len(phone_book)):
        if phone_book[0] in phone_book[i]:
            return False
    return True