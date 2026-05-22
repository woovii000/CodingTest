def solution(str1, str2):
    for i in range(len(str1)):
        str1 = str1[i] + str2[i]
    return str1