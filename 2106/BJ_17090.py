import collections
import sys

def dfs(y, x):
    global cnt
    q = [(y, x)]
    course = set()
    course.add((y, x))

    while q:
        y, x = q.pop()

        if dp[y][x]:
            for value in course:
                dp[value[0]][value[1]] = 1
            cnt += 1
            return

        if area[y][x] == 'U':
            y -= 1
        elif area[y][x] == 'R':
            x += 1
        elif area[y][x] == 'D':
            y += 1
        else:
            x -= 1
        
        if (not (0 <= y < n)) or (not (0 <= x < m)):
            for value in course:
                dp[value[0]][value[1]] = 1
            cnt += 1
            return

        elif (dp[y][x] == -1):
            for value in course:
                dp[value[0]][value[1]] = -1
            return

        elif dp[y][x]:
            for value in course:
                dp[value[0]][value[1]] = 1
            cnt += 1
            return

        elif not visited[y][x]:
            visited[y][x] = 1
            course.add((y, x))
            q.append((y, x))

    for value in course:
        dp[value[0]][value[1]] = -1
    return


n, m = map(int, sys.stdin.readline().split())
area = [sys.stdin.readline() for _ in range(n)]
dp = [[0] * m for _ in range(n)]
cnt = 0
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        if (dp[i][j] == -1):
            continue
        elif dp[i][j]:
            cnt += 1
            continue
        dfs(i, j)
print(cnt)