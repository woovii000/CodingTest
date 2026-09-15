def solution(people, limit):
    # 최소한 움직이기
    people.sort()
    count, left, right = 0,0,len(people)-1
    
    while left <= right:
        
        if people[left]+people[right] > limit:
            count += 1
            right -= 1
        else:
            count += 1
            left += 1
            right -= 1
    return count