from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    start_idx = deque()
    area[i][j] = 2
    visited = [[0] * area_num for _ in range(area_num)]

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (0 <= ny < area_num) and (0 <= nx < area_num):
                if area[ny][nx] == 1:
                    q.append((ny, nx))
                    area[ny][nx] = 2
                elif not area[ny][nx]:
                    start_idx.append((y, x))
                    break

    while start_idx:
        y, x = start_idx.popleft()
        if visited[y][x] >= min_bridge:
            return
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (0 <= ny < area_num) and (0 <= nx < area_num) and (not visited[ny][nx]):
                if area[ny][nx] == 1:
                    return visited[y][x]
                elif not area[ny][nx]:
                    start_idx.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1


area_num = int(input())
area = [list(map(int, input().split())) for _ in range(area_num)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_bridge = area_num * 2

for i in range(area_num):
    for j in range(area_num):
        if area[i][j] == 1:
            bridge_num = bfs(i, j)
            if bridge_num:
                min_bridge = min(bridge_num, min_bridge)

print(min_bridge)