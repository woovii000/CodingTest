def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    answer = -1
    count = 0
    while scoville :
        scoville.sort()
        # scoville의 모든 원소 >= K -> answer
        if ?? 모두 >= K:
            answer = count
            break
        # 섞기
        if len(scoville) >=2:
            new = scoville[0]+(scoville[1]*2)
            scoville.pop(0)
            scoville.pop(1)
            scoville.insert(0,new)
        # 마지막 섞었을 때 < K -> -1
        if len(scoville)==1 and scoville[-1] < K:
            break
        count += 1   
            
    return answer