from collections import deque

def direction(before, after):
    if before == after:
        return 0
    elif (before, after) == (1, 2) or (before, after) == (2, 1) or (before, after) == (3, 4) or (before, after) == (4, 3):
        return 2
    else:
        return 1

def bfs(i, j, dir, visited):
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]

    q = deque()
    q.append((i, j, dir, 0))
    visited[i][j][dir] = True

    while q:
        x, y, pos, count = q.popleft()

        if x == ex-1 and y == ey-1:
            return count + direction(pos, ed)

        for i in range(1, 4):
            nx, ny = x + dx[pos] * i, y + dy[pos] * i

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny][pos]:
                continue
                
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] != 1:
                visited[nx][ny][pos] = True
                q.append((nx, ny, pos, count + 1))
            else:
                break

        for i in range(1, 5):
            if not visited[x][y][i]:
                visited[x][y][i] = True
                q.append((x, y, i, count + direction(pos, i)))


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[[False for _ in range(5)] for _ in range(N)] for _ in range(M)]

sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

result = bfs(sx-1, sy-1, sd, visited)
print(result)