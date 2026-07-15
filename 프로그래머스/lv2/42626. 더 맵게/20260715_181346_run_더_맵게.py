import heapq

def solution(scoville, K):
    answer = 0
    # 힙 -> 자동 정렬
    heapq.heapify(scoville) # list -> heap
    while scoville :
        if heapq[0] >= K:
            return answer
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville,first+second*2)
        answer += 1
    return answer