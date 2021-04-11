def solution(idx):
    global max_status

    if idx == N:
        max_status = max(max_status, sum(res))
    else:
        for i in range(N):
            if (not visit[i]) and (status[idx][i] != 0):
                res[idx] = status[idx][i]
                visit[i] = True
                solution(idx + 1)
                visit[i] = False


case = int(input())
N = 11
for _ in range(case):
    status = [list(map(int, input().split())) for _ in range(N)]
    res = [0] * N
    visit = [0] * N
    max_status = 0
    solution(0)
    print(max_status)