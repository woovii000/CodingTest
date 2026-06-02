def solution(participant, completion):
    # 인원 많음 - 안 뛴 사람 추리기. 동명이인 있을 수 있음**
    # 1) 이중 for 동일하면 pop -> 남은 인원 있는 배열 출력 => 배열크기 변경**
    # 2) 리스트 복사 후, 있다면, 복사한 list에서 pop*-> remove
    # 배열 복사
    answer = participant[:]
    for i in range(len(completion)):
        if completion[i] in answer:
            answer.remove(completion[i])
    return answer[0]