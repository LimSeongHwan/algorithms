import sys
from collections import deque

input = sys.stdin.readline
n, t = map(int, input().split())
time = 0
signal_dict = dict()
signal_dict[1] = [(-1, 0), (0, 1), (1, 0)]
signal_dict[2] = [(-1, 0), (0, -1), (0, 1)]
signal_dict[3] = [(1, 0), (0, -1), (-1, 0)]
signal_dict[4] = [(1, 0), (0, 1), (0, -1)]
signal_dict[5] = [(-1, 0), (0, 1)]
signal_dict[6] = [(0, -1), (-1, 0)]
signal_dict[7] = [(0, -1), (1, 0)]
signal_dict[8] = [(0, 1), (1, 0)]
signal_dict[9] = [(1, 0), (0, 1)]
signal_dict[10] = [(-1, 0), (0, 1)]
signal_dict[11] = [(-1, 0), (0, -1)]
signal_dict[12] = [(0, -1), (1, 0)]
visited = [[0] * n for _ in range(n)]
now = (0, 0)
max_cnt = 0
signals = []
temp_list = []
for i in range(1, (n ** 2) + 1):
    temp = list(map(int, input().split()))
    temp_list.append(temp)
    if (i % n) == 0:
        signals.append(temp_list)
        temp_list = []
        
def bfs(start_y, start_x):
    global max_cnt
    visited[start_y][start_x] = 1
    q = deque([(start_y, start_x, 0)])
    cnt = 1

    while q:
        y, x, time = q.popleft()
        if time == t:
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            signal = signals[y][x][time % 4]
            way = signal_dict[signal]
            for j in range(len(way)):
                ny = y + way[j][0]
                nx = x + way[j][1]

                if (0 <= ny < n) and (0 <= nx <n) and (not visited[ny][nx]):
                    visited[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx, time + 1))

bfs(0, 0)
print(max_cnt)