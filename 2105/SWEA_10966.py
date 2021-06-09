from collections import deque

def bfs(water_idx):
    q = deque(water_idx)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    now_dist = 1
    total_dist = 0

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()

            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x

                if (0 <= ny < row) and (0 <= nx < col) and (visited[ny][nx] == -1):
                    visited[ny][nx] = now_dist
                    q.append((ny, nx))
        now_dist += 1

    for value in visited:
        total_dist += sum(value)

    return total_dist


case = int(input())
for tc in range(1, case + 1):
    row, col = map(int, input().split())
    water_idx = []
    area = []
    visited = [[-1] * col for _ in range(row)]
    

    for i in range(row):
        line = list(input())
        for j in range(col):
            if line[j] == 'W':
                water_idx.append((i, j))
                visited[i][j] = 0
        area.append(line)

    print('#{} {}'.format(tc, bfs(water_idx)))