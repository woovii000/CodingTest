def solution(participant, completion):
    # 안 뛴 사람 1명 찾아내기**
    # 인원 많음, 동명이인 있을 수 있음**
    # 1) 이중 for 동일하면 pop -> 남은 인원 있는 배열 출력 
    # => 배열크기 변경됨, O(n²) | 실패
    # 2) 리스트 복사 후, 있다면, 복사한 list에서 pop*
    # => remove(value)(o), pop(index)(x), O(n²) | 효율성 실패 
    # 3) 정렬 후, 비교 => sort(). i ~ 순차 비교, O(n)
    # 4) Hash
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]