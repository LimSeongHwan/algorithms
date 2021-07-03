def find_bomb():
    bomb_idx = []
    not_bomb_idx = []
    for i in range(r):
        for j in range(c):
            if area[i][j] == 'O':
                bomb_idx.append((i, j))
            else:
                not_bomb_idx.append((i, j))
    return bomb_idx, not_bomb_idx


def plant_bomb(not_bomb_idx):
    global n
    if n == 0:
        return False
    for y, x in not_bomb_idx:
        area[y][x] = 'O'
    n -= 1
    return True


def bomb(bomb_idx):
    global n
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    if n == 0:
        return
    for y, x in bomb_idx:
        area[y][x] = '.'
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if (0 <= ny < r) and (0 <= nx < c) and (area[ny][nx] == 'O'):
                area[ny][nx] = '.'
    n -= 1


r, c, n = map(int, input().split())
area = [list(input()) for _ in range(r)]
n -= 1

while n != 0:
    bomb_idx, not_bomb_idx = find_bomb()
    if plant_bomb(not_bomb_idx):
        bomb(bomb_idx)

for value in area:
    print(''.join(value))