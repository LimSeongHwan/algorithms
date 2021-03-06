from collections import deque


def bfs(y, x):
    time_area = [[-1] * col for _ in range(row)]
    max_time = 0
    time_area[y][x] = 0
    q = deque([[y, x]])

    while q:
        y, x = q.popleft()

        if (y > 0) and (time_area[y - 1][x] == -1) and (area[y - 1][x] == "L"):
            time_area[y - 1][x] = time_area[y][x] + 1
            q.append([y - 1, x])
        if (y < row - 1) and (time_area[y + 1][x] == -1) and (area[y + 1][x] == "L"):
            time_area[y + 1][x] = time_area[y][x] + 1
            q.append([y + 1, x])
        if (x > 0) and (time_area[y][x - 1] == -1) and (area[y][x - 1] == "L"):
            time_area[y][x - 1] = time_area[y][x] + 1
            q.append([y, x - 1])
        if (x < col - 1) and (time_area[y][x + 1] == -1) and (area[y][x + 1] == "L"):
            time_area[y][x + 1] = time_area[y][x] + 1
            q.append([y, x + 1])

    return time_area[y][x]


row, col = map(int, input().split())
area = []
max_time = 0
start = []

for i in range(row):
    info = list(input())
    area.append(info)
    for j in range(col):
        if info[j] == "L":
            start.append([i, j])

for i in range(len(start)):
    max_time = max(max_time, bfs(start[i][0], start[i][1]))

print(max_time)