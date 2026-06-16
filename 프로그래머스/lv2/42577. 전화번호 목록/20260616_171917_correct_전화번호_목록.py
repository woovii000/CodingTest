def solution(phone_book):
    # phone_book의 원소 중에 번호 겹침o -> False
    # 겹침x -> True
    # 포인트: 접두어* -> startswith()
    # 이중 for → O(n²) => 오답
    # 정렬 후, 비교: 정렬 → O(n log n)
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True