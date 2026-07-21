def solution(people, limit):
    # 최소한 움직이기
    people = sorted(people) # 무게 오름차순 정렬
    count, left = 0, 0
    right = len(people)-1

    while left<=right :
        # 최대 무게와 최소 무게의 합 <= limit :: 2명 이송
        current = people[right]
        # 만약 2명 무게 합 제한보다 큼 -> 1명만 이동
        if people[right] + people[left] > limit:
            count += 1
            right -= 1
        else:
            count += 1 
            right -= 1
            left += 1

    return count