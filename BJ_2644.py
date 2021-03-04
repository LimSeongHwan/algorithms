from collections import deque


def bfs(start, end):
    q = deque([start])
    while q:
        v = q.popleft()
        if v not in visited:
            visited[v] = 1
            for next_node in adj[v]:
                if next_node not in visited:
                    if next_node == end:
                        return distance[v] + 1
                    distance[next_node] = distance[v] + 1
                    q.append(next_node)
    return -1


node_num = int(input())
start_node, end_node = map(int, input().split())
adj_num = int(input())
visited = dict()
distance = [0] * (node_num + 1)
adj = [[] for _ in range(node_num + 1)]
for j in range(adj_num):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(start_node, end_node))
