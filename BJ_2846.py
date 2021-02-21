int(input())
arr = list(map(int, input().split()))
max_val = 0

for i in range(len(arr)-1):
    now = arr[i]

    for j in range(i + 1, len(arr)):
        if now < arr[j]:
            now = arr[j]
        else:
            break

    max_val = max(max_val, now - arr[i])
print(max_val)