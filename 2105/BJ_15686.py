from collections import deque
from copy import deepcopy


def solution(idx, start, choice):
    global min_dist
    if idx == chick:
        value = bfs(choice, deepcopy(area))
        if value:
            min_dist = min(value, min_dist)
        return
    for i in range(start, len(chick_idx)):
        solution(idx + 1, i + 1, choice + [chick_idx[i]])


def bfs(start_idx, area):
    cnt = 0
    total_dist = 0
    q = deque(start_idx)
    
    while q:
        y, x, dist = q.popleft()

        if dist >= min_dist:
            return
            
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (0 <= ny < area_len) and (0 <= nx < area_len):
                if area[ny][nx] == 1:
                    cnt += 1
                    total_dist += dist
                    area[ny][nx] = -2
                elif (not area[ny][nx]):
                    area[ny][nx] = -1
                else:
                    continue

                q.append((ny, nx, dist + 1))

        if cnt == house_cnt:
            return total_dist
        
            
area_len, chick = map(int, input().split())
area = []
chick_idx = []
house_cnt = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(area_len):
    line = list(map(int, input().split()))
    for j in range(area_len):
        if line[j] == 2:
            chick_idx.append((i, j, 1))
            line[j] = 0
        elif line[j]:
            house_cnt += 1
    area.append(line)

min_dist = 0xffffff
solution(0, 0, [])
print(min_dist)