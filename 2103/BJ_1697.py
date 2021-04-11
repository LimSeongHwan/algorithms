from collections import deque


def bfs(soobin, dongsaeng):
    time_table = [0] * 100001
    q = deque([soobin])

    while q:
        v = q.popleft()

        if v == dongsaeng:
            print(time_table[v])
            return

        for now_idx in [(v - 1), (v + 1), (v * 2)]:
            if (0 <= now_idx <= max_idx) and (not time_table[now_idx]):
                q.append(now_idx)
                time_table[now_idx] = time_table[v] + 1


idx_soobin, idx_dongsaeng = map(int, input().split())
max_idx = 100000
bfs(idx_soobin, idx_dongsaeng)