from collections import deque


def bfs(v):
    visited = dict()
    visited[v] = 1
    q = deque([v])
    level = 0
    
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            for next_pos in adj[v]:
                if next_pos not in visited:
                    visited[next_pos] = 1
                    q.append(next_pos)
        if q:
            level += 1

    return level

member_num = int(input())
adj = [[] for _ in range(member_num + 1)]
leader_score = 999
leader_list = []

while True:
    x, y = map(int, input().split())
    if x == -1:
        break
    adj[x].append(y)
    adj[y].append(x)

for i in range(1, member_num + 1):
    score = bfs(i)

    if leader_score > score:
        leader_list = []
        leader_score = score
        leader_list.append(i)

    elif leader_score == score:
        leader_list.append(i)

leader_list.sort()
print(leader_score, len(leader_list))
print(' '.join(map(str, leader_list)))