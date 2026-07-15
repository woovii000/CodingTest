def solution(scoville, K):
    answer = -1
    count = 0
    scoville.sort() # 정렬
    mix = [] #  섞은 음식
    while len(scoville) || len(mix):
        if len(mix)==0: # mix 비었을 떄
            if scoville[0] >= K: # scoville[0]>=K
                answer = count
                break
            mix.append(scoville[0]+scoville[1]*2)
            del scoville[0:2]
        elif scoville[0] >= mix[0]:
            if mix[0] >= K:
                answer = count
                break
            mix.append(mix[0]+scoville[0]*2)
            scoville.pop(0)
            mix.pop(0)
        else:
            if scoville[0] >= K:
                answer = count
                break
            mix.append(scoville[0]+mix[0]*2)
            scoville.pop(0)
            mix.pop(0)
        count += 1
    return answer