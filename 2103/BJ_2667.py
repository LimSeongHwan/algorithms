from collections import deque
import time


def dfs(y, x):
    global cnt
    area[y][x] = 0
    cnt += 1
    for i in range(len(dy)):
        ny = dy[i] + y
        nx = dx[i] + x
        if (
            (0 <= ny <= (area_length - 1))
            and (0 <= nx <= (area_length - 1))
            and area[ny][nx]
        ):
            dfs(ny, nx)
    return cnt


def bfs(y, x):
    q = deque([[y, x]])
    cnt = 0
    while q:
        y, x = q.popleft()
        if area[y][x]:
            area[y][x] = 0
            cnt += 1

            for i in range(len(dy)):
                ny = dy[i] + y
                nx = dx[i] + x
                if (
                    (0 <= ny <= (area_length - 1))
                    and (0 <= nx <= (area_length - 1))
                    and area[ny][nx]
                ):
                    q.append([ny, nx])
    return cnt


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
area_num = 0
res = []
area = []
area_length = int(input())
for i in range(area_length):
    area.append(list(map(int, input())))

for i in range(area_length):
    for j in range(area_length):
        if area[i][j]:
            cnt = 0
            res.append(bfs(i, j))
            area_num += 1

res.sort()
print(area_num)
print("\n".join(map(str, res)))
