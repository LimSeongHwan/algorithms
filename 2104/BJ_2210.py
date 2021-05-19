def dfs(start, arr):
    if len(arr) == 6:
        res.add(tuple(arr))
        return
    y, x = start
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if (0 <= ny < 5) and (0 <= nx < 5):
            dfs((ny, nx), arr + [area[ny][nx]])


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
res = set()
area = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        dfs((i, j), [])
print(len(res))