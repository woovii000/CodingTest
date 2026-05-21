def solution(my_string, overwrite_string, s):
    my_string[s:len(overwrite_string)] = overwrite_string 
    return my_string