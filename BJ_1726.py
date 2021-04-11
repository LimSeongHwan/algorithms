from collections import deque


def bfs(start_y, start_x, course):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    area[start_y][start_x] = 3
    q = deque([[start_y, start_x, course]])

    while q:
        y, x, course = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (0 <= ny < row) and (0 <= nx < col) and (not area[ny][nx]):
                if (ny == end_y) and (nx == end_x):
                    return course + [(ny, nx)]
                area[ny][nx] = 3
                q.append((ny, nx, course + [(ny, nx)]))


def direction_cnt(start_direction, move_direction):
    global change_flag
    change_flag = True
    if move_direction == 4 or move_direction == 3:
        if start_direction == 1 or start_direction == 2:
            return 1
        else:
            return 2
    elif start_direction == 4 or start_direction == 3:
        return 1
    else:
        return 2


row, col = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(row)]
start_y, start_x, start_direction = map(int, input().split())
end_y, end_x, end_direction = map(int, input().split())
start_y -= 1
start_x -= 1
end_y -= 1
end_x -= 1
move_cnt = 0
res = bfs(start_y, start_x, [(start_y, start_x)])
change_flag = False

if res:
    for i in range(1, len(res)):
        if (res[i - 1][1] < res[i][1]) and (start_direction != 1):
            move_cnt += direction_cnt(start_direction, 1)
            start_direction = 1
        elif (res[i - 1][1] > res[i][1]) and (start_direction != 2):
            move_cnt += direction_cnt(start_direction, 2)
            start_direction = 2
        elif (res[i - 1][0] < res[i][0] and (start_direction != 3)):
            move_cnt += direction_cnt(start_direction, 3)
            start_direction = 3
        elif (res[i - 1][0] > res[i][0]) and (start_direction != 4):
            move_cnt += direction_cnt(start_direction, 4)
            start_direction = 4
        else:
            change_flag = False

        if change_flag:
            move_cnt += 1

if start_direction != end_direction:
    move_cnt += direction_cnt(start_direction, end_direction)
print(move_cnt)