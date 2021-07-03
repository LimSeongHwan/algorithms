import sys
from collections import deque

input = sys.stdin.readline
train_num, order = map(int, input().split())
trains = [0] + [deque([0]) * 20 for _ in range(train_num)]
train_check = set()

for _ in range(order):
    input_value = list(map(int, input().split()))

    if len(input_value) == 3:
        do, train, idx = input_value
        idx -= 1
    else:
        do, train = input_value
    
    if do == 1:
        if not trains[train][idx]:
            trains[train][idx] = 1
    elif do == 2:
        if trains[train][idx]:
            trains[train][idx] = 0
    elif do == 3:
        trains[train].pop()
        trains[train].appendleft(0)
    else:
        trains[train].popleft()
        trains[train].append(0)

for i in range(1, train_num + 1):
    train_check.add(str(trains[i]))

print(len(train_check))



0 1 0 1 0 -> 모두 한 칸씩 뒤로 -> 맨 뒤에 있는 0을 맨 앞으로 옮긴다
0 0 1 0 1

0 1 0 1 0 -> 모두 한 칸씩 앞으로 -> 맨 앞에 있는 0을 맨 뒤로 옮긴다
1 0 1 0 0