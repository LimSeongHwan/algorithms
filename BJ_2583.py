from collections import deque


def bfs(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque([[y, x]])
    area[y][x] = 1
    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < row) and (0 <= nx < col) and (not area[ny][nx]):
                area[ny][nx] = 1
                q.append([ny, nx])
                cnt += 1

    return cnt


row, col, square_num = map(int, input().split())
area = [[0] * col for _ in range(row)]
sub_area = 0
area_list = []

for _ in range(square_num):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            area[i][j] = 1

for i in range(row):
    for j in range(col):
        if area[i][j] == 0:
            sub_area += 1
            area_list.append(bfs(i, j))

print(sub_area)
print(" ".join(map(str, sorted(area_list))))