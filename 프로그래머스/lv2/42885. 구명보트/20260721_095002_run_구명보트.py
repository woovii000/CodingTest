def solution(people, limit):
    # 2pointer?
    people = sorted(people) # 오름차순 정렬
    count = 0 # 옮긴 횟수
    left = 0 # 정렬 후 맨앞 idx
    right = len(people)-1 # 정렬 후 맨뒤 idx
    while left != right:
        current = 0 
        current += people[right] 
        # 최대 탑승인원: 2명
        if people[right] + people[left] > limit:
            right -= 1
            count += 1
        else:
            right -= 1
            left += 1
            count += 1
            
    return count