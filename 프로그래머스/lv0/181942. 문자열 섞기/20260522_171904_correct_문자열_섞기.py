def solution(str1, str2):
    answer = ""
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    # enumerate(str1) 사용해보기
    return answer