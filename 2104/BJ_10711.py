from collections import deque 

def bfs(start_idx):
    dy = [-1,-1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    q = deque(start_idx)
    wave = -1
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(8):
                ny = dy[i] + y
                nx = dx[i] + x
                if (0 <= ny < row) and (0 <= nx < col) and area[ny][nx]:
                    area[ny][nx] -= 1
                    if area[ny][nx] == 0:
                        q.append((ny, nx))
        wave += 1
    return wave

row, col = map(int, input().split())
area = []
start_idx = []
for i in range(row):
    info = list(input())
    for j in range(col):
        if info[j] == '.':
            info[j] = 0
            start_idx.append((i, j))
        else:
            info[j] = int(info[j])
    area.append(info)

res = bfs(start_idx)
print(res)