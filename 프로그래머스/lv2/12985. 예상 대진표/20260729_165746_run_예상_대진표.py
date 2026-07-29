def solution(n,a,b):
    count = 0
    # 라운드 마다 번호 바뀜 -> a,b 업데이트*
    while a != b:
        a = (a+1)//2    
        b = (b+1)//2
        count += 1
    return count