def solution(bridge_length, weight, truck_weights):
    in_bridge = []
    fin = []
    i_idx, t_idx, count = 0, 0, 0
    # 도로탈출 트럭 과 총 트럭 수 동일하기 전까지
    while len(fin) < len(truck_weights): 
        sum = 0
        # 시간 +1
        count += 1 
        
        # 다리위 모든 트럭 경과 시간 +1
        for truck in in_bridge:
            truck[1] += 1
        
        # 가장 앞 트럭 경과시간 >= bridge_length
        if not in_bridge.isEmpty() and in_bridge[i_idx][1] >= bridge_length:
            fin.append(in_bridge[i_idx][0])
            i_idx += 1
            
        for i in range(i_dix, len(in_bridge)):
            sum += in_bridge[i][0]
            
        if t_idx < len(truck_weights) and (sum + truck_weights[t_idx]) <= weight:
            in_bridge.append([truck_weights[t_idx],0])
            t_idx += 1
            
    return count