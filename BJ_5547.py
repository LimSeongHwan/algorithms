def dfs(y, x):
    global res
    q = [(y, x)]
    visited[y][x] = 1

    while q:
        y, x = q.pop()
        for i in range(6):
            ny = y + dy[i]
            if y % 2:
                nx = x + dx[i]
            else:
                nx = x + dx2[i]

            if (0 <= ny < (row + 2)) and (0 <= nx < (col + 2)) and (not area[ny][nx]) and (not visited[ny][nx]):
                visited[ny][nx] = 1
                q.append((ny, nx))

                for j in range(6):
                    nny = ny + dy[j]
                    if ny % 2:
                        nnx = nx + dx[j]
                    else:
                        nnx = nx + dx2[j]

                    if (0 <= nny < (row + 2)) and (0 <= nnx < (col + 2)) and area[nny][nnx]:
                        res += 1


col, row = map(int, input().split())
area = [[0] * (col + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(row)] + [[0] * (col + 2)]
res = 0
dy = [-1, -1, 0, 0, 1, 1]
dx = [1, 0, -1, 1, 0, 1]
dx2 = [-1, 0, -1, 1, 0, -1]
visited = [[0] * (col + 2) for _ in range(row + 2)]
dfs(0, 0)
print(res)