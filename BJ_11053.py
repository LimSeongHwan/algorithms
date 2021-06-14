arr_length = int(input())
arr = list(map(int, input().split()))
dp = [1] * arr_length

for i in range(arr_length - 1):
    for j in range(i + 1, arr_length):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
