def solution(my_string):
    answer = []
    # sort(), [-i:],
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    return answer.sort()