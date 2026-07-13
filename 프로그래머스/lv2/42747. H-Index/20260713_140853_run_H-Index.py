def solution(citations):
    citations.sort()
    # h보다 큰 원소가 h개 있어야 함. 
    for i in range(1,len(citations)+1):
        answer = 0
        # i 보다 큰 원소가 citantions에 얼마나 있는지 확인
        for j in range(len(citations)):
            if i <= citations[j]:
                answer += 1
        if i == answer:
            return answer