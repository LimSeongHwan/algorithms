import random
arr = random.sample(range(1, 31), 20)

for i in range(len(arr)-1):
    min_val = i
    for j in range(i+1, len(arr)):
        if arr[min_val] > arr[j]:
            min_val = j
    arr[i], arr[min_val] = arr[min_val], arr[i]
    print(min_val, arr)