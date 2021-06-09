from collections import deque


def pipe_direct(direct):
    if direct == 1:
        return (0, 1, 2, 3)
    elif direct == 2:
        return (0, 1)
    elif direct == 3:
        return (2, 3)
    elif direct == 4:
        return (0, 3)
    elif direct == 5:
        return (1, 3)
    elif direct == 6:
        return (1, 2)
    return (0, 2)


def bfs(y_idx, x_idx, direct, time):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque([(y_idx, x_idx, direct)])
    area[y_idx][x_idx] = 8
    cnt = 1

    while q:
        for _ in range(len(q)):
            y, x, direct = q.popleft()
            directs = pipe_direct(direct)

            for direct in directs:
                ny = dy[direct] + y
                nx = dx[direct] + x
                flag = False

                if (0 <= ny < row) and (0 <= nx < col) and area[ny][nx] and (area[ny][nx] != 8):
                    if direct == 0:
                        if (area[ny][nx] not in [3, 4, 7]):
                            flag = True
                    elif direct == 1:
                        if area[ny][nx] not in [3, 5, 6]:
                            flag = True
                    elif direct == 2:
                        if area[ny][nx] not in [2, 6, 7]:
                            flag = True
                    else:
                        if area[ny][nx] not in [2, 4, 5]:
                            flag = True

                    if flag:
                        q.append((ny, nx, area[ny][nx]))
                        area[ny][nx] = 8
                        cnt += 1

        time -= 1
        if time == 1:
            return cnt
    return cnt

case = int(input())

for tc in range(1, case + 1):
    row, col, y_idx, x_idx, time = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(row)]
    
    if time == 1:
        print('#{} {}'.format(tc, 1))
    else: 
        res = bfs(y_idx, x_idx, area[y_idx][x_idx], time)
        print('#{} {}'.format(tc, res))