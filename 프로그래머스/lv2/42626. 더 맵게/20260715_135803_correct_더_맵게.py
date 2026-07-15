def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    answer = -1
    count = 0
    while scoville :
        scoville.sort() # 정렬
        # scoville 처음 >= K -> 이후도 다 K이상
        if scoville[0] >= K:
            answer = count
            break
        # 마지막 섞었을 때 < K -> -1
        elif len(scoville)==1:
            break
        # 섞기
        new = scoville[0]+(scoville[1]*2)
        del scoville[0:2] # 한꺼번에 지우기
        scoville.insert(0,new)
        count += 1
            
    return answer