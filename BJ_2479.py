from collections import deque

def bfs(start):
    visited = [False] * (case_num + 1)
    visited[start] = True
    q = deque([[start, [start]]])
    while q:
        v, arr = q.popleft()
        for next_pos in dist_info[v]:
            if not visited[next_pos]:
                if next_pos == end:
                    return arr + [end]
                visited[next_pos] = True
                q.append((next_pos, arr + [next_pos]))
    return -1
    
            
def haeming_dist(arr1, arr2):
    incorrect = 0
    for i in range(case_length):
        if arr1[i] != arr2[i]:
            incorrect += 1
    if incorrect == 1:
        return True
    else:
        return False


case_num, case_length = map(int, input().split())
case = [0] + [input() for _ in range(case_num)]
dist_info = [[] for _ in range(case_num + 1)]
for i in range(1, case_num):
    for j in range(i + 1, case_num + 1):
        if haeming_dist(case[i], case[j]):
            dist_info[i].append(j)
            dist_info[j].append(i)

start, end = map(int, input().split())
res = bfs(start)
if res == -1:
    print(res)
else:
    print(' '.join(map(str, res)))