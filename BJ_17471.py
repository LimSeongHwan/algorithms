def dfs(target):
    if len(target) == 1:
        return True

    visited = dict()
    start_val = target[0]
    compare_list = target[1:]
    visited[start_val] = 1
    q = [start_val]
    cnt = 1

    while q:
        v = q.pop()

        for next_pos in adj[v]:
            if (next_pos in compare_list) and (next_pos not in visited):
                visited[next_pos] = 1
                q.append(next_pos)
                cnt += 1

    if cnt == len(target):
        return True
    return False

def solution(idx, start):
    if idx == num_len:
        divide_res.append(list(res))
    else:
        for i in range(start, area_num):
            res[idx] = area[i]
            solution(idx + 1, i + 1)


area_num = int(input())
area = [i for i in range(1, area_num + 1)]
area_population = [0] + list(map(int, input().split()))
area_divide = [[] for _ in range(2)]
adj = dict()
min_population = 1001

for i in range(1, area_num + 1):
    info = list(map(int, input().split()))
    adj[i] = info[1:]

for num_len in range(1, area_num):
    divide_res = []
    res = [0 for _ in range(num_len)]
    solution(0, 0)
    
    for j in range(len(divide_res)):
        divide_other = [k for k in area if k not in divide_res[j]]
        
        if dfs(divide_res[j]) and dfs(divide_other):
            sum_val = 0
            
            for data in divide_res[j]:
                sum_val += area_population[data]
            for data in divide_other:
                sum_val -= area_population[data]
            min_population = min(abs(sum_val), min_population)

if min_population != 1001:
    print(min_population)
else:
    print(-1)