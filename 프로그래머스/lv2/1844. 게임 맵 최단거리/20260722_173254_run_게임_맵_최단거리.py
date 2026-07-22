from collections import deque

def solution(maps):

    rows = len(maps) # maps의 x길이
    cols = len(maps[0]) # maps의 y길이

    queue = deque()
    queue.append((0,0))
    # 상하좌우 이동 정보
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue :
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i] # 이동 시, x좌표
            ny = y+dy[i] # 이동 시, y좌표

            # 범위 외에 있는가
            if nx<0 or ny<0 or nx>rows or ny>cols:
                continue
            # 이동 칸 == 벽
            if maps[nx][ny] == 0:
                continue
            # 이동 칸 - 안 갔는지
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1 # 이동 칸 수 누적
                queue.append((nx,ny))

    answer = maps[rows-1][cols-1] # 목적지=거리수
    # 거리수 == 1 -> 도착x
    if answer == 1:
        return -1
    return answer
