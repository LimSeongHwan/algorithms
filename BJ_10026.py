from collections import deque
import copy


def bfs(y, x, area, color1, color2):
    q = deque([[y, x]])
    area[y][x] = "X"
    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if (
                (0 <= ny <= area_length - 1)
                and (0 <= nx <= area_length - 1)
                and ((area[ny][nx] == color1) or (area[ny][nx] == color2))
            ):
                area[ny][nx] = "X"
                q.append([ny, nx])


area_length = int(input())
area = [list(input()) for _ in range(area_length)]
area2 = copy.deepcopy(area)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
area_num = 0
area_num2 = 0

for i in range(area_length):
    for j in range(len(area[0])):
        if area[i][j] != "X":
            area_num += 1
            bfs(i, j, area, area[i][j], area[i][j])
        if area2[i][j] == "B":
            area_num2 += 1
            bfs(i, j, area2, area2[i][j], area2[i][j])
        elif area2[i][j] != "X":
            area_num2 += 1
            bfs(i, j, area2, "R", "G")

print(area_num, area_num2)
