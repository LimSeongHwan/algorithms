def find_bingo(data):
    bingo_cnt = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i != 0:
                if j != 0:
                    continue
            print(i, j)
            if data[i][j] == "X":
                for k in range(len(dy)):
                    ny = dy[k] + i
                    nx = dx[k] + j
                    count_X = 1
                    while (
                        (0 <= ny <= (len(data) - 1))
                        and (0 <= nx <= (len(data[0]) - 1))
                        and data[ny][nx] == "X"
                    ):
                        count_X += 1
                        ny += dy[k]
                        nx += dx[k]
                        if count_X == 5:
                            bingo_cnt += 1
    return bingo_cnt


area_length = 5
X_area = [["."] * area_length for _ in range(area_length)]
call_cnt = 5
called_nums = []
num_idx = dict()
bingo_flag = False
call_time = 0
dy = [1, 0, 1, 1]
dx = [0, 1, -1, 1]

for i in range(area_length):
    bingo_nums = list(map(int, input().split()))
    for j in range(len(bingo_nums)):
        num_idx[bingo_nums[j]] = [i, j]

for i in range(call_cnt):
    called_nums.append(list(map(int, input().split())))

for i in range(len(called_nums)):
    for j in range(len(called_nums[0])):
        call_time += 1
        y, x = num_idx[called_nums[i][j]]
        X_area[y][x] = "X"
        if call_time >= 12:
            if find_bingo(X_area) >= 3:
                print(call_time)
                bingo_flag = True
                break
    if bingo_flag:
        break