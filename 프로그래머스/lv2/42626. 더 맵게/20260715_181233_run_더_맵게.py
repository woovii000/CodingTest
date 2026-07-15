import heapq

def solution(scoville, K):
    answer = 0
    # 힙 -> 자동 정렬
    heapq.heapify(scoville) # list -> heap
    while scoville :
        if heapq[0] >= K:
            return answer
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first+second*2
            heapq.heappush(scoville,new)\
            answer += 1
    return answer