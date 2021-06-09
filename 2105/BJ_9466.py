def dfs(start, q):
    global num

    while q:
        v = q.pop()
        
        if visited[select[v]]:
            if select[v] in team:
                num -= (len(team) - team.index(select[v]))
                return
        else:
            visited[select[v]] = 1
            q.append(select[v])
            team.append(select[v])


for _ in range(int(input())):
    num = int(input())
    select = [0] + list(map(int, input().split()))
    visited = [0] * (num + 1)
    
    for i in range(1, len(select)):
        if not visited[i]:
            team = [i]
            visited[i] = 1
            dfs(i, [i])
            
    print(num)