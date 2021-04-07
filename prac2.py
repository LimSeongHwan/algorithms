def bfs(s):
    S = [[s, str(s)]]
    while S:
        ls = S.pop(0)
        p, path = ls[0], ls[1]   # p는 현재 코드, path는 지금까지의 해밍경로(문자열)
        for i in range(1, n+1):
            if not visit[i]:          # 방문하지 않은 모든 코드에 대해
                cnt = 0
                for j in range(m):    # 해밍거리가 몇인지 체크
                    if arr[i][j] != arr[p][j]:
                        cnt += 1
                if cnt == 1:                   # 해밍거리가 1일 경우
                    if i == goal:              # 찾고자하는 코드와 같은 경우
                        path += str(i)
                        return ' '.join(path)
                    visit[i] = 1               # 찾는 코드가 아니면 visit체크
                    new_path = path + str(i)   # 지금까지의 경로에 현재 i 코드 추가
                    S.append([i, new_path])    # 덱에 추가
    return -1

n, m = map(int, input().split())
arr = [''] + [input() for _ in range(n)]
start, goal = map(int, input().split())   # start는 출발하는 코드, goal은 찾고자하는 코드
visit = [1] + [0]*n    # 해밍코드번호가 1부터 시작해서 n+1크기의 visit리스트 생성
visit[start] = 1       # 처음 시작하는 코드는 visit 처리
res = bfs(start)
if res == -1:
    print(-1)
else:
    print(res)