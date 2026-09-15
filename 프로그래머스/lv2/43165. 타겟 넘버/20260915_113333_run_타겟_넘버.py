def solution(numbers, target):
    answer = 0
    def depth(index, result):
        nonlocal answer
        
        if index == len(numbers):
            if result == target:
                answer += 1
            return answer
        
        depth(index+1, result+numbers[index])
        depth(index+1, result-numbers[index])
        
    depth(0,0)