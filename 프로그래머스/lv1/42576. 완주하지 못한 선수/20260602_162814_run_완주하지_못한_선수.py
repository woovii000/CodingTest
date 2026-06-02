def solution(participant, completion):
    # 인원 많음 - 안 뛴 사람 추리기. 동명이인 있을 수 있음**
    # 1) 이중 for 동일하면 pop -> 남은 인원 있는 배열 출력
    # 2) 
    for person in completion:
        answer = [x for x in participant if x != person]
    return answer