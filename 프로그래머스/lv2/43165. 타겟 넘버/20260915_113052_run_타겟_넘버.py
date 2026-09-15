def solution(numbers, target):
    answer = 0
    def depth(index, result):
        nonlocal answer
        
        if result == target:
            answer += 1
            break
        
        depth(index+1, result+numbers[index])
        depth(index+1, result+numbers[index])
        
        
    depth(0,0)
    return answer