def solution(brown, yellow):
    # g*s 형태(g >= s) -> 조합 찾기
    # 카펫 패턴 - i**2 , n*m
    # b, y
    carpet = brown + yellow
    answer = []
    def pattern(ga, se):   
        nonlocal answer
        
        if ga*se == carpet and ga-se >=0:
            answer.append([ga, se])
            return
        
        pattern(ga+1, se)
        pattern(ga+1, se+1)
    
    pattern(0,0)
    return answer