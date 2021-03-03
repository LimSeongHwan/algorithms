max_val = 0
max_idx = 0
for i in range(1, 6):
    scores = list(map(int, input().split()))
    if sum(scores) > max_val:
        max_val = sum(scores)
        max_idx = i

print(max_idx, max_val)