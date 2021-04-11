from collections import deque


def bfs(start_list):
    dl = [0, 0, 0, 0, -1, 1]
    dy = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    tomato_cnt = 0
    max_time = 0
    q = deque(start_list)

    for l, y, x in q:
        tomato_area[l][y][x] = -1

    while q:
        l, y, x = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            nl = l + dl[i]
            if (
                (0 <= ny <= row - 1)
                and (0 <= nx <= col - 1)
                and (0 <= nl <= floor - 1)
                and (not tomato_area[nl][ny][nx])
            ):
                tomato_area[nl][ny][nx] = -1
                q.append([nl, ny, nx])
                time[nl][ny][nx] = time[l][y][x] + 1
                tomato_cnt += 1

                if time[nl][ny][nx] > max_time:
                    max_time = time[nl][ny][nx]

    return max_time, tomato_cnt


col, row, floor = map(int, input().split())
time = [[[0] * col for _ in range(row)] for _ in range(floor)]
tomato_area = [[] for __ in range(floor)]
start_list = []
sum_tomato = 0

for i in range(floor):
    for j in range(row):
        info = list(map(int, input().split()))
        tomato_area[i].append(info)
        for k in range(len(info)):
            if info[k] == 1:
                start_list.append([i, j, k])
            if info[k] == 0:
                sum_tomato += 1

if sum_tomato == 0:
    print(0)
else:
    max_time, tomato_cnt = bfs(start_list)
    if tomato_cnt != sum_tomato:
        print(-1)
    else:
        print(max_time)