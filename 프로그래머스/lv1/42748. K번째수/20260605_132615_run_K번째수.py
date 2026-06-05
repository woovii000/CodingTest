def solution(array, commands):
    answer = []
    for i, j, k in commands:
        slide = array[i:j]
        slide.sort()
        answer.append(slide[k])
    return answer