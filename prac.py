def dfs(y, x, pipe_state, area):
    global cnt

    if (y == (area_length - 1)) and (x == (area_length - 1)):
        cnt += 1
        return

    for i in range(len(dy)):
        if (i == 0) and (pipe_state == 1):
            continue
        elif (i == 1) and (pipe_state == 0):
            continue
        elif (i == 2) and ((x + 1) <= area_length - 1) and ((y + 1) <= (area_length - 1)) and (area[y][x + 1] or area[y + 1][x]):
            continue
        
        ny = dy[i] + y
        if (ny >= area_length):
            continue
        nx = dx[i] + x
        if (nx >= area_length):
            continue

        if (not area[ny][nx]):
            dfs(ny, nx, i, area)


dy = [0, 1, 1]
dx = [1, 0, 1]
cnt = 0
area_length = int(input())
area = [list(map(int, input().split())) for _ in range(area_length)]
dfs(0, 1, 0, area)
print(cnt)