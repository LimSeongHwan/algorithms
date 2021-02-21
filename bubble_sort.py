import random
arr = random.sample(range(1, 31), 20)

for i in range(len(arr)-1):
    for j in range(1, len(arr)-i):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        print(arr)
            
        