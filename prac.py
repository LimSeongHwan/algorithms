heights = []
check = [False] * 9
res = []
sum_flag = False
for i in range(9):
    heights.append(int(input()))


def solution(idx):
    global sum_flag
    if sum_flag:
        return

    if idx == 9:
        sum_val = 0
        res = []
        for i in range(9):
            if check[i]:
                sum_val += heights[i]
                res.append(heights[i])

        if sum_val == 100 and len(res) == 7:
            res.sort()
            sum_flag = True
            print("\n".join(map(str, res)))
        return

    check[idx] = True
    solution(idx + 1)
    check[idx] = False
    solution(idx + 1)


solution(0)