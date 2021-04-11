from collections import deque


def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    for next_pos in adj[v]:
        if next_pos not in visited:
            dfs(next_pos)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v not in visited:
            visited[v] = 1
            print(v, end=" ")
            for next_pos in adj[v]:
                if next_pos not in visited:
                    q.append(next_pos)


node_num, adj_num, start = map(int, input().split())
visited = dict()
adj = [[] for _ in range(node_num + 1)]
for _ in range(adj_num):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
for value in adj:
    value.sort()
dfs(start)
print()
visited = dict()
bfs(start)