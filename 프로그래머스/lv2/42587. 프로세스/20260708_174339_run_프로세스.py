def solution(priorities, location):
                
# 흐름 - 맨 앞에서 하나씩 꺼내며 뒤로 보내는 과정
# while
# [(2,0), (1,1), (3,2), (2,3)] 로 (우선순위, 원래 인덱스) 만들기 -> enumerate()
# [][0] 가 더 큰게 있다? -> pop(idx) + append() -> for문 직접 , max(x for x in __)
# 제일 크다? pop(idx) + count++
# [][1] == location -> return
    
    queue = []
    count = 0
    for index, value in enumerate(priorities):
        queue.append((value,index))
    while queue:
        m = max(x for x in queue)
        if queue[?][0] >= m:
            pop()
            count += 1
        else:
            pop()
            append()
        if queue[?][1] == location:
            return count
        