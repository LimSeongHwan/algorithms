from collections import deque


def bfs(start_list):
    q = deque(start_list)
    tomato_cnt = 0
    max_time = 0
    for y, x in q:
        tomato_area[y][x] = -1

    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if (
                (0 <= ny <= row - 1)
                and (0 <= nx <= col - 1)
                and (not tomato_area[ny][nx])
            ):
                tomato_area[ny][nx] = -1
                q.append([ny, nx])
                time[ny][nx] = time[y][x] + 1
                tomato_cnt += 1

                if time[ny][nx] > max_time:
                    max_time = time[ny][nx]

    return max_time, tomato_cnt


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
col, row = map(int, input().split())
tomato_area = []
start_list = []
time = [[0] * col for _ in range(row)]
tomato_zero = 0

for i in range(row):
    info = list(map(int, input().split()))
    tomato_area.append(info)
    for j in range(len(info)):
        if info[j] == 1:
            start_list.append([i, j])
        if info[j] == 0:
            tomato_zero += 1

max_time, tomato_cnt = bfs(start_list)
if tomato_cnt != tomato_zero:
    print(-1)
else:
    print(max_time)