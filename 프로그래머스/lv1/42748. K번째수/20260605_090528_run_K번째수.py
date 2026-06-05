def solution(array, commands):
    answer = []
    for i, j, k in commands:
        slide = array[i:j+1]
        slide.sort()
        answer.append(slide[k])
    return "".join(answer)