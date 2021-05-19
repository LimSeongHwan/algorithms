def dfs(y, x, dig_status, now_height, length):
    global max_val

    if length > max_val:
        max_val = length

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if (0 <= ny < area_length) and (0 <= nx < area_length) and (not visited[dig_status][ny][nx]):
            if now_height > area[ny][nx]:
                visited[dig_status][y][x] = 1
                dfs(ny, nx, dig_status, area[ny][nx], length + 1)
                visited[dig_status][y][x] = 0
            elif (not dig_status) and now_height <= area[ny][nx] and (area[y][x] > area[ny][nx] - dig):
                visited[1][y][x] = 1
                dfs(ny, nx, 1, area[y][x] - 1, length + 1)
                visited[1][y][x] = 0


case = int(input())
for tc in range(1, case + 1):
    area_length, dig = map(int, input().split())
    visited = [[[0] * area_length for _ in range(area_length)] for __ in range(2)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    area = []
    start = []
    max_val = 0
    max_height = 0
    
    for i in range(area_length):
        temp = list(map(int, input().split()))
        area.append(temp)
        for j in range(area_length):
            if temp[j] > max_height:
                start = []
                max_height = temp[j]
                start.append((i, j))
            elif temp[j] == max_height:
                start.append((i, j))

    for idx in start:
        dfs(idx[0], idx[1], 0, area[idx[0]][idx[1]], 1)
        
    print('#{} {}'.format(tc, max_val))    