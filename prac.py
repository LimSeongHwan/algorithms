def haeming_dist(arr1, arr2):
    incorrect = 0
    for i in range(m):
        if arr1[i] != arr2[i]:
            incorrect += 1
    if incorrect == 1:
        return True
    else:
        return False


def bfs(s):
    S = [[s, [s]]]
    while S:
        p, path = S.pop(0)
        for next_pos in dist_info[p]:
            if not visit[next_pos]:          # 방문하지 않은 모든 코드에 대해
                if next_pos == goal:              # 찾고자하는 코드와 같은 경우
                    path += [next_pos]
                    return ' '.join(map(str, path))
                visit[next_pos] = 1               # 찾는 코드가 아니면 visit체크
                S.append([next_pos, path + [next_pos]])    # 덱에 추가
    return -1

n, m = map(int, input().split())
arr = [''] + [input() for _ in range(n)]
start, goal = map(int, input().split())   # start는 출발하는 코드, goal은 찾고자하는 코드
visit = [1] + [0]*n    # 해밍코드번호가 1부터 시작해서 n+1크기의 visit리스트 생성
visit[start] = 1       # 처음 시작하는 코드는 visit 처리
dist_info = [[] for _ in range(n + 1)]
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if haeming_dist(arr[i], arr[j]):
            dist_info[i].append(j)
            dist_info[j].append(i)
print(bfs(start))