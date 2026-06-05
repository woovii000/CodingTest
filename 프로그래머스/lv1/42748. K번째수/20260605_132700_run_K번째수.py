def solution(array, commands):
    answer = []
    for i, j, k in commands:
        slide = array[i-1:j]
        slide.sort()
        answer.append(slide[k-1])
    return answer