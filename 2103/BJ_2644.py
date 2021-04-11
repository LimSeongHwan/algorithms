from collections import deque


def bfs(start, distance):
    q = deque([[start, 0]])
    while q:
        v, distance = q.popleft()
        if v not in visited:
            visited[v] = 1
            for next_node in adj[v]:
                if next_node not in visited:
                    if next_node == end_node:
                        return distance + 1
                    q.append((next_node, distance + 1))
    return -1


node_num = int(input())
start_node, end_node = map(int, input().split())
adj_num = int(input())
visited = dict()
adj = [[] for _ in range(node_num + 1)]
for j in range(adj_num):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(start_node, 0))
