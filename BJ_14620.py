def solution(y, cnt, pay):
    global min_pay
    if pay > min_pay:
        return

    if cnt == 3:
        if pay < min_pay:
            min_pay = pay
        return

    else:
        for i in range(y, area_length - 1):
            for j in range(1, area_length - 1):
                if (not flower[i][j]) and (not flower[i - 1][j]) and (not flower[i + 1][j]) and (not flower[i][j - 1]) and (not flower[i][j + 1]):
                    sum_val = 0
                    for k in range(5):
                        ny = dy[k] + i
                        nx = dx[k] + j
                        flower[ny][nx] = 1
                        sum_val += area[ny][nx]
                    solution(i, cnt + 1, pay + sum_val)
                    for k in range(5):
                        ny = dy[k] + i
                        nx = dx[k] + j
                        flower[ny][nx] = 0

area_length = int(input())
area = [list(map(int, input().split())) for _ in range(area_length)]
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
min_pay = 0xffffff
flower = [[0] * area_length for _ in range(area_length)]

for y in range(1, area_length - 1):
    for x in range(1, area_length - 1):
        solution(y, 0, 0)

print(min_pay)