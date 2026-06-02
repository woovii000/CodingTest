def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if is_suffix.equals(my_string[-i]):
            return 1
        else
            return 0