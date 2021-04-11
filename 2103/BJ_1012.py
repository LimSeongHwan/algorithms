from collections import deque


def bfs(y, x):
    q = deque([[y, x]])
    area[y][x] = 0
    while q:
        y, x = q.popleft()
        for k in range(len(dy)):
            ny = y + dy[k]
            nx = x + dx[k]
            if (0 <= ny <= row - 1) and (0 <= nx <= col - 1) and area[ny][nx]:
                area[ny][nx] = 0
                q.append([ny, nx])


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
case = int(input())
for _ in range(case):
    col, row, cabbage_num = map(int, input().split())
    area = [[0] * col for i in range(row)]
    earthworm_num = 0
    for i in range(cabbage_num):
        x, y = map(int, input().split())
        area[y][x] = 1
    for i in range(row):
        for j in range(col):
            if area[i][j]:
                earthworm_num += 1
                bfs(i, j)

    print(earthworm_num)
