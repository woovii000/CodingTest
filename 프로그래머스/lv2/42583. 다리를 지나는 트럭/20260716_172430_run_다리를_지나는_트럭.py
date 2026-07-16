def solution(bridge_length, weight, truck_weights):
    in_bridge = []
    fin = []
    i_idx, t_idx, count = 0, 0, 0
    # 도로탈출 트럭 과 총 트럭 수 동일하기 전까지
    while len(fin) != len(truck_weights): 
        count += 1 # 1초 후,
        # 다리 건너는 트럭(다리는 더 갈지말지)
        if sum(in_bridge) <= weight:
            in_bridge.append((truck_weights[t_idx],0))
            t_idx += 1
        # 다리 다 건넌 트럭 
        for i in range(len(i_idx,in_bridge+1)):
            in_bridge[i][1] += 1
            if in_bridge[i_idx][1] >= bridge_length:
                fin.append(in_bridge[i_idx][0])
                i_idx += 1
    return count