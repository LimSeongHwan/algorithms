import sys
from copy import deepcopy

sys.setrecursionlimit(100000000)

def change_direct(now, direct):
    move = ''
    if now == 0:
        if direct == 1:
            move += 'LL'
        elif direct == 2:
            move += 'L'
        elif direct == 3:
            move += 'R'
    elif now == 1:
        if direct == 0:
            move += 'LL'
        elif direct == 2:
            move += 'L'
        elif direct == 3:
            move += 'R'
    elif now == 2:
        if direct == 0:
            move += 'R'
        elif direct == 1:
            move += 'L'
        elif direct == 3:
            move += 'LL'
    elif now == 3:
        if direct == 0:
            move += 'L'
        elif direct == 1:
            move += 'R'
        elif direct == 2:
            move += 'LL'

    return move


def dfs(start_y, start_x, direct, cnt, control):
    global min_control
    if cnt == shap_cnt:
        if len(control) < min_len:
            min_control = deepcopy(control)
        return

    for i in range(4):
        ny = dy[i] + start_y
        nx = dx[i] + start_x

        if (0 <= ny < r) and (0 <= nx < c) and (area[ny][nx] == "#") and (area[ny - 1][nx] == "#"):
            visited[ny][nx] = 1
            visited[ny - 1][nx] = 1
            if direct == 0:
                dfs(ny, nx, 0, cnt + 2, control + ['A'])
            else:
                move = change_direct(direct, 0)
                dfs(ny, nx, 0, cnt + 2, control + [move])
            visited[ny][nx] = 0
            visited[ny - 1][nx] = 0

        elif (0 <= ny < r) and (0 <= nx < c) and (area[ny][nx] == "#") and (area[ny + 1][nx] == "#"):
            visited[ny][nx] = 1
            visited[ny + 1][nx] = 1
            if direct == 1:
                dfs(ny, nx, 1, cnt + 2, control + ['A'])
            else:
                move = change_direct(direct, 1)
                dfs(ny, nx, 1, cnt + 2, control + [move])
            visited[ny][nx] = 0
            visited[ny + 1][nx] = 0

        elif (0 <= ny < r) and (0 <= nx < c) and (area[ny][nx] == "#") and (area[ny][nx - 1] == "#"):
            visited[ny][nx] = 1
            visited[ny][nx - 1] = 1
            if direct == 2:
                dfs(ny, nx, 2, cnt + 2, control + ['A'])
            else:
                move = change_direct(direct, 2)
                dfs(ny, nx, 2, cnt + 2, control + [move])
            visited[ny][nx] = 0
            visited[ny][nx - 1] = 0

        elif (0 <= ny < r) and (0 <= nx < c) and (area[ny][nx] == "#") and (area[ny][nx + 1] == "#"):
            visited[ny][nx] = 1
            visited[ny][nx + 1] = 1
            if direct == 3:
                dfs(ny, nx, 0, cnt + 2, control + ['A'])
            else:
                move = change_direct(direct, 3)
                dfs(ny, nx, 3, cnt + 2, control + [move])
            visited[ny][nx] = 0
            visited[ny][nx + 1] = 0


input = sys.stdin.readline
r, c = map(int, input().split())
area = []
start_idx = []
visited = [[0] * c for _ in range(r)]
dy = [-2, 2, 0, 0]
dx = [0, 0, -2, 2]
shap_cnt = 0
min_len = 0xffffff
min_control = ''

for i in range(r):
    temp = input()
    area.append(temp)
    for j in range(c):
        if temp[j] == '#':
            start_idx.append((i, j))
            shap_cnt += 1

for start_y, start_x in start_idx:
    for i in range(4):
        visited[start_y][start_x] = 1
        dfs(start_y, start_x, i, 1, [])

print(min_control)
