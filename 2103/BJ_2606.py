def dfs(v):
    global virus_cnt
    visited[v] = True
    for next_node in adj[v]:
        if not visited[next_node]:
            dfs(next_node)
            virus_cnt += 1


computer_num = int(input())
adj_length = int(input())
visited = [False] * (computer_num + 1)
adj = [[] for _ in range(computer_num + 1)]
for _ in range(adj_length):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

virus_cnt = 0
dfs(1)
print(virus_cnt)