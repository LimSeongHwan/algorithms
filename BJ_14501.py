period = int(input())
schedules = []
for _ in range(period):
    time, money = map(int, input().split())
    schedules.append((time, money))
dp = [0] * period

for i in range(period):
    if i + schedules[i][0] <= period:
        dp[i] = schedules[i][1]
        for j in range(i):
            if j + schedules[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + schedules[i][1])
                
print(max(dp))