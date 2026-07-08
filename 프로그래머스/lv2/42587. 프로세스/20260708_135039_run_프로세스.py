def solution(priorities, location):
    # for 
    # idx - location
    # priorities[idx]
    answer = 0
    while len(priorities) != 0:
        if location == priorities.index(max(priorities)):
            return answer+1
        priorities.pop(priorities.index(max(priorities)))
        answer += 1