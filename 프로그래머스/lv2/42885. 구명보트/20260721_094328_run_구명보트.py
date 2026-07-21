def solution(people, limit):
    # 2pointer?
    sorted(people) # 오름차순 정렬
    count = 0 # 옮긴 횟수
    left = 0 # 정렬 후 맨앞 idx
    right = len(people)-1 # 정렬 후 맨뒤 idx
    while left != right:
        if left == right:
            break
        current = 0 
        current += people[right]
        for i in range(left, right):    
            # 최대 탑승인원: 2명
            if people[right] + people[i] > limit:
                right -= 1
                count += 1
                break
            else:
                right -= 1
                left += 1
                count += 1
                break
                
    return count