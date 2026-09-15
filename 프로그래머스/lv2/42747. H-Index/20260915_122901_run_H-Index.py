def solution(citations):
    citations.sort(reverse=True)
    # 65310
    for i, citation in citations:
        if citation < i:
            return i-1
    
    return len(citations)
    
            