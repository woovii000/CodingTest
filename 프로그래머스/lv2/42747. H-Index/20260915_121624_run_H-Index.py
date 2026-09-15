def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # 65310
    for i, citation in citations:
        if i+1 <= citation:
            answer = i+1
    
    return answer
    
            