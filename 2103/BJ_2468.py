from collections import deque
from copy import deepcopy


def bfs(y, x, height, area):
    q = deque([[y, x]])
    area[y][x] = 0

    while q:
        y, x = q.popleft()

        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if (
                (0 <= ny < area_length)
                and (0 <= nx < area_length)
                and (area[ny][nx] > height)
            ):
                area[ny][nx] = 0
                q.append([ny, nx])


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
area_length = int(input())
area = [list(map(int, input().split())) for _ in range(area_length)]
max_sub_area = 0

for i in range(101):
    copy_area = deepcopy(area)
    sub_area = 0

    for j in range(area_length):
        for k in range(area_length):
            if copy_area[j][k] > i:
                sub_area += 1
                bfs(j, k, i, copy_area)

    if sub_area > max_sub_area:
        max_sub_area = sub_area

print(max_sub_area)
