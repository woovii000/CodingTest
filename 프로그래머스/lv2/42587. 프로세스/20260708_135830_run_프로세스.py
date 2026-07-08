def solution(priorities, location):
    # for 
    # idx - location
    # priorities[idx]
    # 주의! idx 앞 부터 빼는게 아닌 뒤부터 뺸다. pop()은 뒤에서부터 뺀다
    answer = 0
    while len(priorities) != 0:
        if location == priorities.index(max(priorities)):
            return answer+1
        priorities.pop(priorities.index(max(priorities)))
        answer += 1