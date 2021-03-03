horizon, vertical = map(int, input().split())
cut_val = int(input())
cut_horizon = [0, vertical]
cut_vertical = [0, horizon]
height = 0
width = 0

for _ in range(cut_val):
    direction, cut_num = map(int, input().split())
    if direction == 0:
        cut_horizon.append(cut_num)
    else:
        cut_vertical.append(cut_num)
cut_horizon.sort()
cut_vertical.sort()

for i in range(1, len(cut_horizon)):
    height = max(height, cut_horizon[i] - cut_horizon[i-1])
for i in range(1, len(cut_vertical)):
    width = max(width, cut_vertical[i] - cut_vertical[i-1])
print(height * width)
