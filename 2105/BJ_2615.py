def find_omok(y, x, color):
    for i in range(len(dy)):
        color_cnt = 1
        color_idx = []
        ny = dy[i] + y
        nx = dx[i] + x
        ny_reverse = -dy[i] + y
        nx_reverse = -dx[i] + x
        color_idx.append([x, y])
        while (0 <= ny <= (height - 1)) and (0 <= nx <= (width - 1)) and (area[ny][nx] == color):
            color_cnt += 1
            color_idx.append([nx, ny])                    
            ny += dy[i]
            nx += dx[i]
        while (0 <= ny_reverse <= (height - 1)) and (0 <= nx_reverse <= (width - 1)) and (area[ny_reverse][nx_reverse] == color):
            return
        if color_cnt == 5:
            color_idx.sort()
            return color_idx[0]

height = 19
width = 19
area = []
dy = [1, 0, 1, 1]
dx = [0, 1, -1, 1]
find_flag = False

for i in range(height):
    area.append(list(map(int, input().split())))

for i in range(height):
    for j in range(width):
        if area[i][j]:
            find_idx = find_omok(i, j, area[i][j])
            if find_idx:
                print(area[i][j])
                print(find_idx[1] + 1, find_idx[0] + 1)
                find_flag = True
                break
    if find_flag:
        break
else:
    print(0)