from collections import deque


def bfs_person(start_y, start_x):
    q = deque([[start_y, start_x]])
    visited = [[0] * col for _ in range(row)]

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            if (y == (row - 1)) or (x == (col - 1)) or (not y) or (not x):
                return visited[y][x] + 1
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if (0 <= ny < row) and (0 <= nx < col) and (area[ny][nx] == '.') and (not visited[ny][nx]):
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

        bfs_fire(start_fire_idx)
    return 'IMPOSSIBLE'


def bfs_fire(start_fire_idx):
    for _ in range(len(start_fire_idx)):
        y, x = start_fire_idx.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (0 <= ny < row) and (0 <= nx < col) and (area[ny][nx] == "."):
                area[ny][nx] = '*'
                start_fire_idx.append((ny, nx))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
case_num = int(input())
for _ in range(case_num):
    area = []
    col, row = map(int, input().split())
    start_fire_idx = deque()
    for i in range(row):
        data = list(input())
        area.append(data)
        for j in range(col):
            if data[j] == '@':
                start_idx = (i, j)
            elif data[j] == '*':
                start_fire_idx.append((i, j))

    bfs_fire(start_fire_idx)
    print(bfs_person(start_idx[0], start_idx[1]))