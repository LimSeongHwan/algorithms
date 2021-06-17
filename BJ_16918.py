def find_bomb():
    bomb_idx = []
    for i in range(r):
        for j in range(c):
            if area[i][j] == 'O':
                bomb_idx.append((i, j))
    return bomb_idx


def plant_bomb():
    for i in range(r):
        for j in range(c):
            if area[i][j] == '.':
                area[i][j] = 'O'


def bomb(bomb_idx):
    for y, x in bomb_idx:
        area[y][x] = '.'
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if (0 <= ny < r) and (0 <= nx < c) and (area[ny][nx] == 'O'):
                area[ny][nx] = '.'
            

r, c, n = map(int, input().split())
area = [list(input()) for _ in range(r)]
bomb_idx = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n -= 1

while True:
    if n != 0:
        bomb_idx = find_bomb()
    if n != 0:
        plant_bomb()
        n -= 1
    if n != 0:
        bomb(bomb_idx)
        n -= 1
    if n == 0:
        for value in area:
            print(''.join(value))
        break
