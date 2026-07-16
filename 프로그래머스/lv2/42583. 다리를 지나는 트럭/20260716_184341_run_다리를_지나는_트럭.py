def solution(bridge_length, weight, truck_weights):
    in_b = []
    count, idx, now_weight = 0, 0, 0

    while () :
        count += 1 # 경과시간+1

        for truck in in_b:
            truck[1] += 1 # 다리 위 모든 트럭 경과 시간+1

        # 다리 위에 트럭이 있는지 && 다리 위 맨 앞 트럭이 경과 시간이 지났는지
        if in_b and in_b[idx][1] >= bridge_length:
            fin_t = in_b.pop(0) # 다리 위 맨 앞 트럭 정보 빼기
            now_weight -= fin_t[0] # 다리 위 맨 앞 트럭의 무게 빼기

        # 대기 중인 트럭이 있는지 && 현재 다리 위 무게 + 새로 넣을 트럭 무게 합 <= 제한 무게
        if idx < len(truck_weights) and now_weight + bridge_length[idx] <= weight:
            in_b.append([bridge_length[idx], 0])
            now_weigtht += bridge_length[idx]

    return count 