from collections import deque
from copy import deepcopy


def solution(idx, start):
    if idx == 3:
        archer_pos.append((list(res)))
    else:
        for i in range(start, col):
            res[idx] = arr[i]
            solution(idx + 1, i + 1)

def bfs(archer_pos, attack_range, area):
    global kill_enemy
    q = deque([archer_pos])
    dy = [1, 0, 0]
    dx = [0, -1, 1]

    while q:
        if attack_range == 1:
            return kill_enemy
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny <= row - 1) and (0 <= nx <= col - 1) and (area[ny][nx] == 1):
                area[ny][nx] = 0
                kill_enemy += 1

        attack_range -= 1


row, col, attack_range = map(int, (input().split()))
main_area = [list(map(int, input().split())) for _ in range(row)]
main_area.append([0] * col)
archer_pos = []
res = [0] * 3
arr = [i for i in range(col)]
solution(0, 0)
most_kill_enemy = 0

for pos in archer_pos:
    for idx in pos:
        kill_enemy = 0
        area = deepcopy(main_area)
        for i in range(row - (attack_range - 1), -1, -1):
            most_kill_enemy = max(bfs(row, 5), most_kill_enemy)





            


