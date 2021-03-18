from collections import deque
from copy import deepcopy


def bfs(i, j, people_pos):
    global cnt
    people_list = []
    q = [[i, j]]
    people_list.append(people_pos[i][j])
    people_pos[i][j] = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < 5) and (0 <= nx < 5) and people_pos[ny][nx]:
                people_list.append(people_pos[ny][nx])
                if len(people_list) == 7:
                    S_cnt = 0

                    for people in people_list:
                        if people == "S":
                            S_cnt += 1
                    if S_cnt >= 4:
                        cnt += 1
                    print(people_list, S_cnt)

                    people_list = []

                people_pos[ny][nx] = 0
                q.append((ny, nx))


cnt = 0
people_pos = [list(input()) for _ in range(5)]
for i in range(5):
    for j in range(5):
        temp_pos = deepcopy(people_pos)
        bfs(i, j, temp_pos)
print(cnt)