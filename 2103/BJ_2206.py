from collections import deque


def bfs(crush, y, x):
    visited = [[[0] * col for _ in range(row)] for __ in range(2)]
    visited[0][0][0] = 1
    q = deque([(crush, y, x)])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        crush, y, x = q.popleft()
        if (y == (row - 1)) and (x == (col - 1)):
            return visited[crush][y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < row) and (0 <= nx < col) and (not visited[crush][ny][nx]):
                if area[ny][nx] == '0':
                    visited[crush][ny][nx] = visited[crush][y][x] + 1
                    q.append((crush, ny, nx))
                elif area[ny][nx] == '1' and not crush:
                    visited[1][ny][nx] = visited[crush][y][x] + 1
                    q.append((1, ny, nx))

    return -1


row, col = map(int, input().split())
area = [list(input()) for _ in range(row)]
print(bfs(0, 0, 0))