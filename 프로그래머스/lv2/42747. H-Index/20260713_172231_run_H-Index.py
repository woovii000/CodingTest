def solution(citations):
    citations.sort()
    # i회 이상 인용된 논문이 i편 이상 -> 그 중 max
    answer = 0
    for i in range(1,len(citations)+1): #1~citations까지
        count = 0
        # i 보다 큰 원소가 citantions에 얼마나 있는지 확인
        for j in range(len(citations)): # 0~idx
            if i <= citations[j]: #
                count += 1 # 인용 i회한 논문의 수 i편
        if i <= count: # i == i회 인용한 논문의 수 => 중에 최대 -> i<=count
            answer = count
    if count == None: 
        return 0
    return answer