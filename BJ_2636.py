from collections import deque


def bfs(y, x):
    visited = dict()
    q = deque([[y, x]])
    visited[(y, x)] = 1

    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < row) and (0 <= nx < col) and (not area[ny][nx]):
                if (ny, nx) not in visited:
                    visited[(ny, nx)] = 1
                    q.append([ny, nx])
    return visited


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
row, col = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(row)]
time_cnt = 0
min_cheese = row * col + 1
visited = bfs(0, 0)
start = 0

while min_cheese != 0:
    cheese_cnt = 0
    start += 1
    for i in range(start, row):
        for j in range(start, col):
            if area[i][j] == 1:
                cheese_cnt += 1
                for k in range(len(dy)):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if (0 <= ny < row) and (0 <= nx < col):
                        if (ny, nx) in visited:
                            area[i][j] = 0
    time_cnt += 1

    if cheese_cnt == 0:
        print(time_cnt - 1)
        print(min_cheese)
        break
    else:
        min_cheese = min(min_cheese, cheese_cnt)
        visited = bfs(0, 0)